Survey.Survey.cssType = "bootstrap";

var surveyJSON ={
   pages:[
      {
         name:"page1",
         elements:[
            {
               type:"radiogroup",
               name:"lama masa study",
               title:"lama masa study",
               isRequired:true,
               requiredErrorText:"lama study harus di isi",
               choices:[
                  {
                     value:"1",
                     text:"4 tahun"
                  },
                  {
                     value:"2",
                     text:"4,5 - 5 Tahun"
                  },
                  {
                     value:"3",
                     text:"5,5 - Tahun"
                  },
                  {
                     value:"4",
                     text:"> 6 Tahun"
                  }
               ]
            },
            {
               type:"radiogroup",
               name:"ipk kelulusan",
               title:"ipk kelulusan",
               isRequired:true,
               choices:[
                  {
                     value:"20",
                     text:"2.00 -2.75"
                  },
                  {
                     value:"21",
                     text:"2.76 - 3,50"
                  },
                  {
                     value:"22",
                     text:"3.51-4.0"
                  }
               ]
            },
            {
               type:"radiogroup",
               name:"masa tunggu untuk mendapat pekerjaan ",
               title:"masa tunggu untuk mendapat pekerjaan ",
               isRequired:true,
               choices:[
                  {
                     value:"5",
                     text:"< 3 Bulan"
                  },
                  {
                     value:"6",
                     text:"3 - 6 bulan"
                  },
                  {
                     value:"7",
                     text:"6 - 12 bulan"
                  },
                  {
                     value:"8",
                     text:"> 12 bulan"
                  }
               ]
            },
            {
               type:"radiogroup",
               name:"cara mendapat pekerjaan pertama",
               title:"cara mendapat pekerjaan pertama",
               isRequired:true,
               choices:[
                  {
                     value:"9",
                     text:"iklan"
                  },
                  {
                     value:"10",
                     text:"internet"
                  },
                  {
                     value:"11",
                     text:"pengumuman di kampus"
                  },
                  {
                     value:"12",
                     text:"koneksi"
                  },
                  {
                     value:"13",
                     text:"lainnya"
                  }
               ]
            },
            {
               type:"radiogroup",
               name:"Penghasilan Pertama",
               title:"Penghasilan Pertama",
               isRequired:true,
               choices:[
                  {
                     value:"14",
                     text:"< 1 Juta"
                  },
                  {
                     value:"15",
                     text:"1 - 2 Juta"
                  },
                  {
                     value:"16",
                     text:"2 - 4 Juta"
                  },
                  {
                     value:"17",
                     text:"> 4 Juta"
                  }
               ]
            }
         ]
      },
      {
         name:"page2",
         elements:[
            {
               type:"radiogroup",
               name:"sesuai dengan pekerjaan",
               title:"sesuai dengan pekerjaan",
               choices:[
                  {
                     value:"18",
                     text:"ya"
                  },
                  {
                     value:"19",
                     text:"tidak"
                  }
               ]
            }
         ]
      }
   ],
   
   showPageNumbers:true,
   showProgressBar:"bottom",
   pagePrevText:"back",
   pageNextText:"next",
   completeText:"complate"
}

   var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
   
   function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
   }

    function sendDataToServer(survey) {
        //send Ajax request to your web server.
        $.ajax({
            type: "POST",
            beforeSend: function(xhr, settings) {
               if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
               }
            },
            data: {
               'data': JSON.stringify(survey.data)
            },
            success: function(data){
               if(data.is_taken == 'succes'){
                  console.log(data);
               }
            }
        })
        //alert("The results are:" + JSON.stringify(survey.data));
    }

    var survey = new Survey.Model(surveyJSON);
    $("#surveyContainer").Survey({
        model: survey,
        onComplete: sendDataToServer
    });
