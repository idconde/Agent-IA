from graph import graph


if __name__ == "__main__":

    print("Expense agent ready")

    while True:

        message = input("\n> ")

        if message == "exit":
            break

        graph.invoke({
            "message": message
        })