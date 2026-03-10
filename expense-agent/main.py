from graph import graph
from db.init_db import init_db

init_db()
if __name__ == "__main__":

    print("Expense agent ready")

    while True:

        message = input("\n> ")

        if message == "exit":
            break

        result = graph.invoke({
            "message": message
        })
        
        print(result["response_message"])