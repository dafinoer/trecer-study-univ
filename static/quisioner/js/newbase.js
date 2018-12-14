Survey.Survey.cssType = "bootstrap";

var surveyJSON = {
    "pages":[
        {
            "name":"page1",
            "elements":[
                {
                    "type":"checkbox",
                    "name":"question1",
                    "title":"seberapa besar metode belajar di bawah ini",
                    "isRequired":true,
                    "choices":[
                        "perkuliahan",
                        "partisipasi",
                        "magang",
                        "praktikum",
                        "kerja lapangan",
                        "diskusi"
                    ]
                },
                {
                    "type":"multipletext",
                    "name":"2321",
                    "title":"Kapan anda mulai mencari pekerjaan ? ",
                    "isRequired":true,
                    "items":[
                        {
                            "name":"text1",
                            "title":"bulan sebelum lulus"
                        },
                        {
                            "name":"text2",
                            "title":"bulan setelah lulus"
                        }
                    ]
                }
            ]
        }
    ]
}

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function sendDataToServer(survey) {
    //send Ajax request to your web server.
    // alert("The results are:" + JSON.stringify(survey.data));
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});