import pywhatkit as pw
text = """Cake or pie? I can tell a lot about you by which one you pick.
It may seem silly, but cake people and pie people are really different.
I know which one I hope you are, but that's not for me to decide.
So, what is it? Cake or pie?"""
pw.text_to_handwriting(text, "handwrite.png", [100,200,150])