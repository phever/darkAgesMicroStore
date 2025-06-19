const CODE_STRING = " Code(s)";
const GOLD_STRING = " Million Gold";
const USD_STRING = " USD";

DataTable.type("da-price", {
  detect: function (data) {
    return typeof data === "string" &&
      data.match(/(\d+)( Million Gold| Code\(s\)| USD)/)
      ? "da-price"
      : null;
  },
  order: {
    pre: function (data) {
      if (data.includes(CODE_STRING)) {
        return Number(data.replace(CODE_STRING, "")) * 1000;
      }
      if (data.includes(USD_STRING)) {
        return Number(data.replace(USD_STRING, "") * 1000);
      }
      return Number(data.replace(GOLD_STRING, ""));
    },
  },
  className: "dt-da-price",
});

$("#shop-table").DataTable({
  responsive: true,
  order: [],
});
