import pyautogui
import time

# Основные клавиши для проверки
keys = [
    "delete", "end", "f12", "f3", "f4", "f5", 
    "f9", "home", "insert", "pagedown", "pageup"
]

# Модификаторы
modifiers = ["ctrlleft", "shiftleft", "ctrlright", "shiftright"]

# Задержка перед началом проверки
print("Проверка начнется через 5 секунд...")
time.sleep(5)

# Прожатие каждой клавиши по отдельности
print("Проверяю одиночные нажатия клавиш...")
for key in keys:
    print(f"Нажимаю: {key}")
    pyautogui.press(key)
    time.sleep(0.5)

# Прожатие комбинаций модификаторов с каждой клавишей
print("Проверяю комбинации клавиш...")
for modifier in modifiers:
    for key in keys:
        print(f"Нажимаю: {modifier} + {key}")
        pyautogui.keyDown(modifier)
        pyautogui.press(key)
        pyautogui.keyUp(modifier)
        time.sleep(0.5)

print("Проверка завершена.")
