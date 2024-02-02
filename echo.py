#echo.py
#3980 SP24
#nknosp
#Assignment1 Python refresher

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    for i in range(repetitions-1):
        print(text)
        if i == 1:
            text = text[-1] # last iteration always 1 letter
            return(text)
        else:
            text = text[1:]

if __name__ == "__main__":
    text = input("yell something at a mountain: ")
    print(echo(text))

