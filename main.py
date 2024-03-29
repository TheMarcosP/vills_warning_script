import keyboard
import time
import pyautogui
import cv2
import numpy as np
import winsound
import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def is_image_on_screen(template_path):
    # Load the image template you want to search for
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    #save screenshot
    screenshot.save('screenshot.png')

    # Convert the screenshot to a NumPy array
    screenshot = np.array(screenshot)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # crop screenshot to only the bottom left corner
    screenshot_gray = screenshot_gray[400:600, 0:200] # height is 


    # Search for the template within the screenshot
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # save result and screenshot
    # cv2.imwrite('screenshot.png', screenshot_gray)
    # cv2.imwrite('result.png', result*255)
    ## print the greatest value (the 'best match') in the result 
    print(np.amax(result))

    # Set a threshold to determine if the template was found
    threshold = 0.65
    location = np.where(result >= threshold)

    # If the template was found, return True
    if len(location[0]) > 0:
        return True
    else:
        return False


def has_passed_n_seconds(n, last_time):
    return time.time() - last_time > n


def main():

    time_between_beeps = 15  # seconds

    hotkey_to_pause_resume = '-'

    hotkey_to_quit = '='
    
    # Path to the image template you want to search for
    image = 'template1.png'

    paused = False

    last_beep_time = time.time()


    print(f"start\npress {hotkey_to_pause_resume} to pause\npress {hotkey_to_quit} to quit")
    winsound.Beep(660, 200)

    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(hotkey_to_pause_resume):  # if key 'q' is pressed 
                paused = not paused
                if paused:
                    print('Paused')
                    play_mp3("pause.mp3")
                    # winsound.Beep(660, 200)
                else:
                    play_mp3("start.mp3")
                    # winsound.Beep(660, 200)
                    last_beep_time = time.time() # reset last beep time
                    print('Resumed')
                time.sleep(0.2)
            
            if keyboard.is_pressed(hotkey_to_quit): 
                print('Quit')
                winsound.Beep(880, 300)
                break 
            
            if not paused and has_passed_n_seconds(time_between_beeps, last_beep_time)  and not is_image_on_screen(image):
                # winsound.Beep(660, 400)
                winsound.PlaySound("make_vils.wav", winsound.SND_FILENAME)
                print("make villagers")
                last_beep_time = time.time()

        except:
            break

        


if __name__ == "__main__":
    main()