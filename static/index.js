const CODE_STRING = " Code(s)";
const GOLD_STRING = " Million Gold";
const USD_STRING = " USD";

DataTable.type("da-price", {
  order: {
    pre: function (data) {
      if (data.includes(CODE_STRING)) {
        return Number(data.replace(CODE_STRING, "")) * 1000;
      }
      if (data.includes(USD_STRING)) {
        return Number(data.replace(USD_STRING, "") * 100);
      }
      return Number(data.replace(GOLD_STRING, ""));
    },
  },
  className: "dt-da-price",
});

DataTable.type("qty", {
  order: {
    pre: function (data) {
      if (typeof data === "string" && data.match(/.*None.*/)) return 0;
      if (
        typeof data === "string" &&
        data.match(/.*I will hunt as many of these as you need*./)
      )
        return 9999;
      return data;
    },
  },
  className: "dt-qty",
});

$("#shop-table").DataTable({
  responsive: true,
  order: [],
  columns: [null, { type: "qty" }, { type: "da-price" }, null],
});
