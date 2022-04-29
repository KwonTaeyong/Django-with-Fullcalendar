// 상단 이동 버튼


// 폰트 사이즈 조절 버튼
function changeFont() {
    document.getElementById('demo').style.fontSize = '50px';
}

function downFont() {
    document.getElementById('demo').style.fontSize = '15px';
}


// 복사 버튼
function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
}


// 일정 날짜 버튼
function date_cha(val) {
    var today = new Date()
    today.setDate(today.getDate() - val)
    $('#date1').val(formatDate(today))

}

// 날짜 date 형식 포맷
function formatDate(date) {

    var d = new Date(date),

        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');

}

// 상단이동
$(window).scroll(function () {
    if ($(this).scrollTop() > 1) {
        $('.scrolltop:hidden').stop(true, true).fadeIn();
    } else {
        $('.scrolltop').stop(true, true).fadeOut();
    }
});

// 페이지 네이션 커스텀 ( grid object , 설정 항목 수 )
function NWpagination(g, n) {
    const page = g.getPagination() // grid의 pagination 객체
    const pagenum = page.getCurrentPage() // 현재 선택한 page
    const perpage = n // 수정할 list 갯수
    page.setItemsPerPage(perpage) // pagination 객체의 list 갯수
    page.setTotalItems(g.getPaginationTotalCount())
    page.movePageTo(pagenum) // pagination 수정후 선택중인 페이지로 이동
    g.setPerPage(perpage) // grid 데이터 재 설정
}


// 요청 url , data, 보여줄 target modal
function modalajax(url, d, tg) {
    $.ajax({
        url: url,
        type: 'get',
        data: {
            action: 'getmodalajax',
            data: d
        },
        success: function (data) {
            for (key in data) {
                if (key === 'HOPE_DELV_DATE') {
                    let newdate = datestrparse(data[key])
                    console.log(newdate)
                    $('#' + key).val(newdate)
                } else {
                    $('#' + key).val(data[key])
                }

            }
            tg.modal('show')
        }
    });
}

function formatDate2() {

    var d = new Date(),

        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// yyyyMMdd str > yyyy-MM-dd str
function datestrparse(str) {
    var y = str.substr(0, 4);
    var m = str.substr(4, 2);
    var d = str.substr(6, 2);
    return `${y}-${m}-${d}`;
}
