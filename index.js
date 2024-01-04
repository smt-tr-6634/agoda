

$(document).ready(function () {
    $("#sort-button").on("click", function () {
      sortCard("rating");
    });
  });

  function sortCard(sortType, reverse = false) {
    var cardsContainer = $(".card-container");
    var cards = cardsContainer.children(".card");

    cards.sort(function (a, b) {
      var valueA = parseFloat($(a).data("rating"));
      var valueB = parseFloat($(b).data("rating"));

      if (sortType === "date") {
        valueA = new Date($(a).find(".text-body-secondary").text());
        valueB = new Date($(b).find(".text-body-secondary").text());
      }

      return reverse ? valueA - valueB : valueB - valueA;
    });

    cardsContainer.empty().append(cards);
  }