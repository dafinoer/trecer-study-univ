Survey.Survey.cssType = "bootstrap";

var k = f3_data();

console.log(f3_data())

var data_pertanyaan_f7 = f7_data();

var data_pertanyaan_f8 = f8_data();

var data_pertanyaan_f9 = f9_data();

var data_pertanyaan_10 = f10_data();

var data_pertanyaan_11 = f11_data();

var data_pertanyaan_12 = f12_data();

var data_pertanyaan_13 = f13_data();

var data_pertanyaan_14 = f14_data();

var data_pertanyaan_15 = f15_data();

var data_pertanyaan_16 = f16_data();

var data_pertanyaan_17 = f17_data();


var surveyJSON = {
    pages: [{
        name: "page1",
        elements: [
            {
                type: "text",
                name: "48",
                title: "berapa bulan anda mencari pekerjaan ketika belum lulus ?",
                isRequired: true,
                validators: [
                    {
                     type: "numeric"
                    },
                    {
                     type: "numeric",
                     text: "must number",
                     minValue: 0
                    }
                ],
                inputType: "number",
                size: 22
            }, {
                type: "text",
                name: "49",
                title: "berapa bulan anda mencari pekerjaan ketika  sudah lulus ?",
                isRequired: true,
                validators: [
                    {
                     type: "numeric"
                    },
                    {
                     type: "numeric",
                     text: "must number",
                     minValue: 0
                    }
                ],
                inputType: "text"
            },
            /*
            {
            type: "multipletext",
            name: "9",
            title: "Kapan anda mulai mencari pekerjaan ? ",
            enableIf: "{2321} ==== /^\\d+$/",
            isRequired: true,
            items: [{
                name: "48",
                title: "bulan sebelum lulus",
                inputType:'number',
            }, {
                name: "49",
                title: "bulan setelah lulus",
                inputType:'number',
            }],
            itemSize: 3
        }, 
        */
        {
            type: "matrix",
            name: "8",
            title:"Menurut anda seberapa besar penekanan pada metode pembelajaran dibawah ini dilaksanakan di program studi anda?",
            isRequired: true,
            columns:[
                   {
                    value: 1,
                    text: "sangat buruk"
                   },
                   {
                    value: 2,
                    text: "buruk"
                   },
                   {
                    value: 3,
                    text: "cukup"
                   },
                   {
                    value: 4,
                    text: "baik"
                   },
                   {
                    value: 5,
                    text: "sangat baik"
                   }
            ],
            rows: [
                {
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
                }
            ]
        },
        {
            type: "checkbox",
            name: "10",
            title: "Bagaimana anda mencari pekerjaan tersebut?",
            isRequired: true,
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
                    value: "125",
                    text: "Lainnya "
                    }   
            ]
        }]
    },
    {
        name: "page2",
        elements: [
         {
          type: "text",
          name: "question2",
          title: "Berapa perusahaan/instansi /institusi yang sudah anda lamar (lewat surat atau e-mail) sebelum anda memperoleh pekerjaan pertama?",
          inputType:"number",
          isRequired: true,
          valueName: "11",
          //isRequired: true
         },
         {
            type: "multipletext",
            name: "12",
            title: "Berapa bulan waktu yang dihabiskan (sebelum dan sesudah kelulusan) untuk memperoleh pekerjaan pertama?",
            isRequired: true,
            //isRequired:true,
            items: k
         },
         {
            type: "multipletext",
            name: "13",
            title: "Berapa banyak perusahaan/instansi/institusi yang merespons/mengundang lamaran anda?",
            isRequired: true,
            items: data_pertanyaan_f7 //[{name:"text2", title:"lorem ipsum"}]
         },
        ]
    },
    {
        name: "page3",
        elements: [
            {
                type: "radiogroup",
                name: "14",
                title: "Apakah anda bekerja saat ini (termasuk kerja sambilan dan wirausaha)?",
                isRequired: true,
                choices: data_pertanyaan_f8  //[{value:"item1", text="ya"}, {value:"item2", text:"tidak"}]
            },
            {
                type: "checkbox",
                name: "15",
                title: "Bagaimana anda menggambarkan situasi anda saat ini?",
                isRequired: true,
                choices: data_pertanyaan_f9 //[{value: "20", text: "lorem"}, {value: "90", text: "ipsum"}]
            },
            {
                type: "radiogroup",
                name: "16",
                title: "Apakah anda aktif mencari pekerjaan dalam 4 minggu terakhir?",
                isRequired: true,
                choices: data_pertanyaan_10 //[{value:"item1", text="ya"}, {value:"item2", text:"tidak"}]
            }
        ]
       },
       {
        name: "page4",
        elements: [
            {
                type: "radiogroup",
                name: "17",
                title: "Apa jenis perusahaan/instansi/institusi tempat anda bekerja sekarang?",
                isRequired: true,
                choices: data_pertanyaan_11, //[{value:"item1", text="ya"}, {value:"item2", text:"tidak"}]
            },
            {
                type: "multipletext",
                name: "18",
                title: "Kira-kira berapa pendapat anda setiap bulannya?",
                isRequired: true,
                items: data_pertanyaan_12    
            },
            {
                type: "matrix",
                name: "19",
                title: "Seberapa erat hubungan antara bidang studi dengan pekerjaan anda saat ini?",
                isRequired: true,
                columns: [
                       {
                        value: 1,
                        text: "sangat buruk"
                       },
                       {
                        value: 2,
                        text: "buruk"
                       },
                       {
                        value: 3,
                        text: "cukup"
                       },
                       {
                        value: 4,
                        text: "baik"
                       },
                       {
                        value: 5,
                        text: "sangat baik"
                       }
                ],
                // choices: [
                //     1,
                //     2,
                //     3,
                //     4,
                //     5
                // ],
                rows: data_pertanyaan_13
            }
        ]
       },
       {
        name: "page5",
        elements: [
            {
                type: "radiogroup",
                name: "20",
                title: "Tingkat pendidikan apa yang tepat/sesuai dengan pendidikan anda, mengapa anda mengambilnya?",
                isRequired: true,
                choices: data_pertanyaan_14 //value text
            },
            
            {
                type: "checkbox",
                name: "21",
                title: "Jika menurut anda pekerjaan anda saat ini tidak sesuai dengan pendidikan anda, mengapa anda mengambilnya?",
                isRequired: true,
                choices: data_pertanyaan_15 //
            },
            {
                type: "matrix",
                name: "22",
                title: "Pada saat lulus, pada tingkat mana kompetensi dibawah ini anda kuasi",
                isRequired: true,
                columns: [
                       {
                        value: 1,
                        text: "sangat buruk"
                       },
                       {
                        value: 2,
                        text: "buruk"
                       },
                       {
                        value: 3,
                        text: "cukup"
                       },
                       {
                        value: 4,
                        text: "baik"
                       },
                       {
                        value: 5,
                        text: "sangat baik"
                       }
                ],
                rows: data_pertanyaan_16 // value texxt
            },
            {
                type: "matrix",
                name: "23",
                title: "Pada saat lulus, bagaimana kontribusi pergruan tinggi dalam hal kompetensi di bawah ini?",
                isRequired: true,
                columns: [
                      {
                        value: 1,
                        text: "sangat buruk"
                       },
                       {
                        value: 2,
                        text: "buruk"
                       },
                       {
                        value: 3,
                        text: "cukup"
                       },
                       {
                        value: 4,
                        text: "baik"
                       },
                       {
                        value: 5,
                        text: "sangat baik"
                       }
                ],
                rows: data_pertanyaan_17 // value texxt
            },

        ]
       },
    ],
    pagePrevText: "back",
    pageNextText: "next",
    showProgressBar:"bottom",
    completeText: "done"
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