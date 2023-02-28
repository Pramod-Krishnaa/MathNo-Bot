from typing import Dict, Any, Text, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMathOperation(Action):
    def name(self) -> Text:
        return "action_math_operation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the operands and operation from the entities
        num1 = float(tracker.get_slot("num1"))
        num2 = float(tracker.get_slot("num2"))
        operation = str(tracker.get_slot("fun"))

        # Perform the math operation based on the user input
        if operation == "addition" or operation == "add" or operation == "Addition" or operation ==  "Add":
            result = num1 + num2
            response = f"BOT- The sum of {num1} and {num2} is {result}."
        elif operation == "subtraction" or operation == "sub" or operation == "Subtraction" or operation == "Sub":
            result = num1 - num2
            response = f"BOT- The difference between {num1} and {num2} is {result}."
        elif operation == "multiplication" or operation == "Multiplication" or operation == "mul" or operation == "Mul":
            result = num1 * num2
            response = f"BOT- The product of {num1} and {num2} is {result}."
        elif operation == "division" or operation == "Division" or operation == "div" or operation == "Div":
            if num2 == 0:
                response = f"BOT- Error. Divisor can't be zero"
            else:
                result = num1 / num2
                response = f"BOT- The quotient of {num1} and {num2} is {result}."
        else:
            response = f"BOT- Sorry, I don't understand that operation."

        # Send the response back to the user
        dispatcher.utter_message(text=response)

        return []
