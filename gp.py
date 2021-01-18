import pyautogui

def main():
    w, h = pyautogui.size()
    x, y = pyautogui.position()
    print("Screen size: width=%s height=%s" % (w, h))
    print("Get Position: X=%s Y=%s" % (x, y))

if __name__ == "__main__":
    main()