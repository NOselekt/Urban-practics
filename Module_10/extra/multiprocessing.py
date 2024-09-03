#CHANGE DIRECTORIES' NAMES


from PIL import Image
import multiprocessing
from queue import Empty
import os


IMAGES_PATHS = [[f'./pictures/{i}.png' for i in range(j*100, j*100+100)] for j in range(10)]

def resize_image(images_paths: list[str], queue: multiprocessing.Queue):
    for image_path in images_paths:
        image = Image.open(image_path)
        image = image.resize((1920, 1080))
        queue.put((image, image_path))

def change_colour(queue: multiprocessing.Queue):
    while True:
        try:
            image, image_path = queue.get(timeout=5)
        except Empty:
            break
        image = image.convert('L')
        try:
            image.save(f"./pictures_changed/{image_path.removeprefix('./pictures/')}")
        except FileNotFoundError:
            os.mkdir('pictures_changed')
        image.save(f"./pictures_changed/{image_path.removeprefix('./pictures/')}")

if '__main__' == __name__:

    queues = []
    resize_processes = []
    change_colour_processes = []


    for i in range(10):
        queues.append(multiprocessing.Queue())

        resize_processes.append(multiprocessing.Process(target=resize_image, args=(IMAGES_PATHS[i],
                                                                                   queues[i])))
        change_colour_processes.append(multiprocessing.Process(target=change_colour, args=(queues[i], )))

    for i in range(10):
        resize_processes[i].start()
        change_colour_processes[i].start()

    for i in range(10):
        resize_processes[i].join()
        change_colour_processes[i].join()