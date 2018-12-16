Survey.Survey.cssType = "bootstrap";

var surveyJSON = {
    pages: [{
        name: "page1",
        elements: [{
            type: "multipletext",
            name: "9",
            title: "Kapan anda mulai mencari pekerjaan ? ",
            enableIf: "{2321} ==== /^\\d+$/",
            isRequired: true,
            items: [{
                name: "text1",
                title: "bulan sebelum lulus"
            }, {
                name: "text2",
                title: "bulan setelah lulus"
            }],
            itemSize: 3
        }, {
            type: "matrixdropdown",
            name: "8",
            title: "Menurut anda seberapa besar penekanan pada metode pembelajaran dibawah ini dilaksanakan di program studi anda?",
            isRequired: true,
            columns: [{
                name: "rating",
                title: "rating",
                isRequired: true
            }],
            choices: [1, 2, 3, 4, 5],
            rows: [{
                value: "39",
                text: "Perkulihan"
            }, {
                value: "40",
                text: "Demonstrasi"
            }, {
                value: "41",
                text: "Partisipasi dalam proyek riset"
            }, {
                value: "42",
                text: "Magang"
            }, {
                value: "43",
                text: "Praktiktum"
            }, {
                value: "44",
                text: "kerja Lapangan"
            }, {
                value: "45",
                text: "Diskusi"
            }]
        }, {
            type: "checkbox",
            name: "10",
            title: "Bagaimana anda mencari pekerjaan tersebut?",
            choices: [
                   {
                    value: "25",
                    text: "Melalui iklan dikoran/majalah, brosur"
                   },
                   {
                    value: "26",
                    text: "Melamar ke perusahaan tanpa mengetahui lowongan yang ada"
                   },
                   {
                    value: "27",
                    text: "Pergi ke bursa/pameran kerja"
                   },
                   {
                    value: "28",
                    text: "Mencari lewat internet/iklan online/milis"
                   },
                   {
                    value: "29",
                    text: "Dihubungi oleh perusahaan"
                   },
                   {
                    value: "30",
                    text: "Menghubungi kemnakertrans"
                   },
                   {
                    value: "31",
                    text: "Menghubungi agen tenaga kerja komersial/swasta"
                   },
                   {
                    value: "32",
                    text: "Memperoleh informasi dari pusat/kantor pengembang karir falkutas/universitas"
                   },
                   {
                    value: "33",
                    text: "Menghubungi kantor kemahasiswaan/hubungi alumni"
                   },
                   {
                    value: "34",
                    text: "Membangun jejaring (network) sejak masih kuliah"
                   },
                   {
                    value: "35",
                    text: "Melalui relasi (misalnya dosen, orangtua, saudara, teman, dll)"
                   },
                   {
                    value: "36",
                    text: "Membangun bisnis sendiri"
                   },
                   {
                    value: "37",
                    text: "Melalui penempatan kerja atau magang"
                   },
                   {
                    value: "38",
                    text: "Bekerja di tempat yang sama dengan tempat kerja sesama kuliah"
                   }, 
                   {
                    value: "item15",
                    text: "Lainnya "
                    }   
            ]
        }]
    }]
}

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function sendDataToServer(survey) {
    //send Ajax request to your web server.
    // alert("The results are:" + JSON.stringify(survey.data));
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
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});