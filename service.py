class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        self.model.create(params["text"], params["Description"])
@app.route("/todo", method=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())