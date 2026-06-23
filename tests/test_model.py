from model import Model, CodingTask

def test_train():
    model = Model()
    tasks = [CodingTask(1, "code1", "domain1"), CodingTask(2, "code2", "domain2")]
    model.train(tasks)
    assert model.get_tasks() == tasks

def test_fine_tune():
    model = Model()
    tasks = [CodingTask(1, "code1", "domain1"), CodingTask(2, "code2", "domain1"), CodingTask(3, "code3", "domain2")]
    model.train(tasks)
    model.fine_tune("domain1")
    assert model.get_tasks() == [tasks[0], tasks[1]]

def test_update():
    model = Model()
    tasks = [CodingTask(1, "code1", "domain1"), CodingTask(2, "code2", "domain2")]
    model.train(tasks)
    new_tasks = [CodingTask(3, "code3", "domain1"), CodingTask(4, "code4", "domain2")]
    model.update(new_tasks)
    assert model.get_tasks() == tasks + new_tasks

def test_save_and_load():
    model = Model()
    tasks = [CodingTask(1, "code1", "domain1"), CodingTask(2, "code2", "domain2")]
    model.train(tasks)
    model.save("model.json")
    loaded_model = Model.load("model.json")
    assert loaded_model.get_tasks() == tasks
