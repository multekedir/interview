from flask import current_app as app


@app.route("/doctors", methods=["GET"])
def doctors():
    pass


@app.route("/appointments/<dr_id>", methods=["GET"])
def appointments(dr_id):
    pass


@app.route("/del_appointment/<app_id>", methods=["DELETE"])
def del_appointment(app_id):
    pass


@app.route("/add_appointment/<dr_id>", methods=["POST"])
def add_appointment(dr_id):
    pass
