from .models import Kategori, Question, Survey


class Tool:

    def __init__(self, value, id_question, id_kategori):
        self.value = value
        self.question = id_question
        self.kategori = id_kategori
    
    @property
    def question_id(self):
        pass
    
    @property
    def kategori_id(self):
        pass
    
    @question_id.getter
    def question_id(self):
        question = Question.objects.get(id=int(self.question))
        return question
    
    @kategori_id.getter
    def kategori_id(self):
        kategori = Kategori.objects.get(id=int(self.kategori))
        return kategori

    def save_database(self):
        
        try:
            survey = Survey(value=self.value, question=self.question_id, kategories=self.kategori_id)

            survey.save()

            # print('Query OOP Succes > {} - {}'.format(self.value, self.question_id))

        except Exception as identifier:
            print(identifier)
