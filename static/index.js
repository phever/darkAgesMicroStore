const CODE_STRING = ' Code(s)'
const GOLD_STRING = ' Million Gold'

DataTable.type('da-price', {
    detect: function (data) {
        return typeof data === 'string' &&
        data.match(/(\d+)( Million Gold| Code\(s\))/)
            ? 'da-price'
            : null;
    },
    order: {
        pre: function (data) {
            if (data.includes(CODE_STRING)) {
                return Number(
                    data.replace(CODE_STRING, '')
                ) * 1000
            }
            return Number(
                data.replace(GOLD_STRING, '')
            );
        }
    },
    className: 'dt-da-price'
});

$('#shop-table').DataTable({
    responsive: true,
});
