class orderdaterender {
    constructor(props) {
        const el = document.createElement('a');
        el.type = 'text'
        el.className = 'test'
        el.href = '#'
        this.el = el;
        this.render(props);
    }

    getElement() {
        return this.el;
    }

    render(props) {
        this.el.text = String(props.value);
    }
}


function readyidlist() {

    let idlist = [];

    $("input:checkbox[name=logbox]").each(function () {

        if ($(this).is(":checked")) {
            idlist.push($(this).attr('id'))
        }
    });

    return idlist
}


function dataSource(url, method, params) {

    return {
        contentType: 'application/json',
        api: {
            readData: {
                url: url,
                method: method,
                initParams: params
            }
        },
    }
}


function orderlisttable(datasource) {
    return new tui.Grid({
        el: document.getElementById('grid'),
        rowHeaders: ['checkbox'], // 체크 박스
        scrollX: true,
        scrollY: false,
        data: data,
        columns: [
            {
                header: '상태',
                name: 'scm_status',
                width: 100,
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '수집일시',
                name: 'REG_DATE',
                width: 150,
                sortable: true,
                align: 'center',
                className: 'bg-light',
                formatter(props) {
                    return props.value.replace('T', ' ')
                }
            },
            {
                header: '출고예정일',
                name: 'HOPE_DELV_DATE',
                sortable: true,
                width: 150,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '주문번호',
                name: 'IDX',
                width: 100,
                sortable: true,
                align: 'center',
                renderer: {
                    type: orderdaterender
                }
            },
            {
                header: '쇼핑몰',
                name: 'MALL_ID',
                width: 150,
                sortable: true,
                align: 'center',
                filter: 'select'
            },
            {
                header: '상품명',
                name: 'PRODUCT_NAME',
                sortable: true,
                align: 'center',
                width: 300,
            },
            {
                header: '옵션명',
                name: 'SKU_VALUE',
                sortable: true,
                align: 'center',
                width: 300,
            },
            {
                header: '수량',
                name: 'P_EA',
                sortable: true,
                filter: 'number',
                width: 50,
                align: 'center',
            },
            {
                header: '주문자',
                name: 'USER_NAME',
                width: 100,
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '주문자 연락처',
                name: 'USER_CEL',
                width: 150,
                sortable: true,
                align: 'center',

            },
            {
                header: '수취인',
                name: 'RECEIVE_NAME',
                sortable: true,
                align: 'center',
                width: 100,
                className: 'bg-light',
            },
            {
                header: '수취인 연락처',
                name: 'RECEIVE_CEL',
                align: 'center',
                width: 150,
                sortable: true,

            },
            {
                header: '주소',
                name: 'RECEIVE_ADDR',
                sortable: true,
                align: 'center',
            },
            {
                header: '배송메세지',
                name: 'DELV_MSG',
                width: 230,
                sortable: true,
                align: 'center',
            },
        ],
        columnOptions: {
            frozenCount: 3,
            frozenBorderWidth: 2,
            resizable: true,
        },

        pageOptions: {
            useClient: true,
            perPage: 20
        },
    });

}


function workmaintable(datasource) {
    return new tui.Grid({
        el: document.getElementById('grid'),
        rowHeaders: ['checkbox'], // 체크 박스
        scrollX: true,
        scrollY: false,
        data: datasource,
        columns: [
            {
                header: '상태',
                name: 'scm_status',
                width: 100,
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '주문자',
                name: 'USER_NAME',
                width: 100,
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '주문자 연락처',
                name: 'USER_CEL',
                width: 150,
                sortable: true,
                align: 'center',
                className: 'bg-light',

            },
            {
                header: '수취인',
                name: 'RECEIVE_NAME',
                sortable: true,
                align: 'center',
                width: 100,
                className: 'bg-light',
            },
            {
                header: '수취인 연락처',
                name: 'RECEIVE_CEL',
                align: 'center',
                width: 150,
                sortable: true,
                className: 'bg-light',

            },

            {
                header: '상품명',
                name: 'PRODUCT_NAME',
                sortable: true,
                align: 'center',
                width: 300,
            },
            {
                header: '옵션명',
                name: 'SKU_VALUE',
                sortable: true,
                align: 'center',
                width: 300,
            },
            {
                header: '수량',
                name: 'P_EA',
                sortable: true,
                filter: 'number',
                width: 50,
                align: 'center',
            },
            {
                header: '주소',
                name: 'RECEIVE_ADDR',
                sortable: true,
                align: 'center',
            },
            {
                header: '배송메세지',
                name: 'DELV_MSG',
                width: 230,
                sortable: true,
                align: 'center',
            },
        ],
        columnOptions: {
            frozenCount: 5,
            frozenBorderWidth: 2,
            resizable: true,
        },

        pageOptions: {
            useClient: true,
            perPage: 20
        },
    })
}

function worklisttable(datasource) {
    return new tui.Grid({
        el: document.getElementById('grid2'),
        rowHeaders: ['checkbox'], // 체크 박스
        scrollX: true,
        scrollY: false,
        data: datasource,
        columns: [
            {
                header: '주문자',
                name: 'USER_NAME',
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '수취인',
                name: 'RECEIVE_NAME',
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '카테고리',
                name: 'OPTION1',
                align: 'center',
                sortable: true,
                className: 'bg-light',

            },

            {
                header: '품목',
                name: 'OPTION2',
                align: 'center',
                sortable: true,
                className: 'bg-light',

            },
            {
                header: '구성품',
                name: 'OPTION3',
                align: 'center',
                sortable: true,
                className: 'bg-light',

            },
            {
                header: '증정',
                name: 'OPTION4',
                align: 'center',
                sortable: true,
                className: 'bg-light',

            },
            {
                header: '쇼핑몰명',
                name: 'MALL_ID',
                align: 'center',
                sortable: true,
                className: 'bg-light',

            },
        ],
        columnOptions: {
            resizable: true,
        },
        pageOptions: {
            useClient: true,
            perPage: 20
        },
    })

}

class categoryrender {
    constructor(props) {
        const el = document.createElement('i');
        el.className = 'bi bi-arrow-right-circle-fill'
        this.el = el;
        this.render(props);
    }

    getElement() {
        return this.el;
    }

    render(props) {
        this.el.text = String('바로보기');
    }
}

function categorytable(datasource) {

    return new tui.Grid({
        el: document.getElementById('grid'),
        rowHeaders: ['rowNum'], // 체크 박스
        scrollX: false,
        scrollY: true,
        data: datasource,
        bodyHeight: 258,
        columns: [
            {
                header: '현재 순위',
                name: 'rank',
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '카테고리 명',
                name: 'name',
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '세부 품목',
                sortable: true,
                align: 'center',
                name: 'product',
                renderer: {
                    type: categoryrender
                }
            },
            {
                header: 'ID',
                name: 'id',
                sortable: true,
                align: 'center',
                hidden: true
            },
        ],
        draggable: true
    });
}

function producttable(datasource) {

    return new tui.Grid({
        el: document.getElementById('grid2'),
        rowHeaders: ['rowNum'], // 체크 박스
        scrollX: false,
        scrollY: true,
        data: datasource,
        bodyHeight: 258,
        bodyWidth: 300,
        columns: [
            {
                header: '현재 순위',
                name: 'rank',
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '품목 명',
                name: 'name',
                sortable: true,
                align: 'center',
                className: 'bg-light',
            },
            {
                header: '세부 품목',
                name: 'id',
                sortable: true,
                align: 'center',
                hidden: true

            },
        ],
        draggable: true
    });
}

function IDtable(datasource) {

    return new tui.Grid({
        el: document.getElementById('grid3'),
        rowHeaders: ['rowNum'], // 체크 박스
        scrollX: false,
        scrollY: true,
        data: datasource,
        bodyHeight: 258,
        bodyWidth: 300,
        columns: [
            {
                header: 'ID',
                name: 'name',
                sortable: true,
                align: 'center',
            },
            {
                header: '공장',
                name: 'name',
                sortable: true,
                align: 'center',
            },
            {
                header: '날짜',
                name: 'create_date',
                sortable: true,
                align: 'center',
            },
        ],
        draggable: true
    });
}

