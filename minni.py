import uiautomator2 as u2
b = u2.connect('emulator-5554')


b(text="Phone").click()
b(text="Contacts").click()

b(text="Create new contact").click()
b(text="First name").set_text("Gayatri")
b(text="Phone").set_text("7890567342")
b(text="SAVE").click()

b.press("back")
b.press("back")
b.press("back")
b.press("back")



b(scrollable=True).scroll(steps=10)
b(text="Clock").click()

b.press("back")

