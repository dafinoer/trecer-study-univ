from django.urls import path

from .views import NimLogin, Quizioner

urlpatterns = [
    # path('login/', login)
    path('alumni/', Quizioner.as_view(), name='quiz-alumni')
]

'''
kategori_data = Kategori.objects.all()

        length_data = len(kategori_data)

        total_page = 5

        first = 0

        page = 2

        pages_lst = []

        pages = {}


        for data in range(0, page):
            outter_dict = {}
            lst_element = []

            for datak in range(first, len(kategori_data)):

                if datak >= total_page:
                    print(datak)
                    total_page += 5
                    first += datak
                    break

                else:
                    dict_to = {}

                    choice_value = []

                    try:
                        get_choice = Question.objects.filter(ketegories=kategori_data[datak].id)

                        for get_data in get_choice:
                            get_dict = {}
                            get_dict["value"] = get_data.id
                            get_dict["text"] = get_data.jawaban

                            choice_value.append(get_dict)

                    except Exception as e:
                        print(e)

                    dict_to["type"] = "radiogroup"
                    dict_to["name"] = kategori_data[datak].tanya
                    dict_to["title"] = kategori_data[datak].tanya
                    dict_to["isRequired"] = 'true'
                    dict_to["requiredErrorText"] = "lama study harus di isi"
                    dict_to["choices"] = choice_value

                    lst_element.append(dict_to)

            outter_dict["name"] = data
            outter_dict["element"] = lst_element
            # outter_dict["sendResultOnPageNext"] = 'true'
            # outter_dict["showPageNumbers"] = 'true'
            # outter_dict["showProgressBar"] = 'bottom'
            # outter_dict["pagePrevText"] = "back"
            # outter_dict["pageNextText"] = "next"
            # outter_dict["completeText"] = "complate"

            # pages_lst.append(outter_dict)
        
        

        # data_dump = json.dumps(pages_lst)
        # load_data_dump = json.loads(data_dump)

        # print(load_data_dump)

        # pages["pages"] = pages_lst
'''