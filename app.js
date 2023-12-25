$(window).scroll(function () {
  if ($(window).scrollTop() > 350) {
    $(".row-search").addClass(" fixed-top ");
    $(".fixed-top").css("top", "0px");
  } else {
    $(".fixed-top").css("top", "-100px");
    $(".row-search").removeClass(" fixed-top");
  }
});

function toggleClass(btn) {
  // Remove 'active' class from all buttons
  $(".cards button").removeClass("active");
  // Add 'active' class to the clicked button
  $(btn).addClass("active");
}

$(document).ready(function () {
  // Fiyata göre sıralama butonuna tıklandığında sıralama yap
  $("#sort-button").on("click", function () {
    sortCards("price");
  });

  // Ratinge göre sıralama butonuna tıklandığında sıralama yap
  $("#sort-by-rating-button").on("click", function () {
    sortCards("rating");
  });
});

function sortCards(sortType) {
  // Kartları istenilen kritere göre sırala
  var cardsContainer = $(".card-container");
  var cards = cardsContainer.children(".card");

  cards.sort(function (a, b) {
    var valueA, valueB;

    if (sortType === "price") {
      valueA = parseFloat($(a).data("price"));
      valueB = parseFloat($(b).data("price"));
    } else if (sortType === "rating") {
      valueA = parseFloat($(a).data("rating"));
      valueB = parseFloat($(b).data("rating"));
    }

    // Fiyat veya ratinge göre sırala
    if (sortType === "price") {
      return valueA - valueB;
    } else if (sortType === "rating") {
      // Rating sıralamasını yüksekten düşüğe sırala
      return valueB - valueA;
    }
  });

  // Sıralanmış kartları tekrar container'a ekle
  cardsContainer.empty().append(cards);
}

// owl courosel
$(".owl-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: false,
  dots: false,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
  },
});

// Custom Next Button
$("#customNextBtn1").click(function () {
  $("#owl-carousel-1").trigger("next.owl.carousel");
});

// Custom Prev Button
$("#customPrevBtn1").click(function () {
  $("#owl-carousel-1").trigger("prev.owl.carousel");
});

$("#customNextBtn2").click(function () {
  $("#owl-carousel-2").trigger("next.owl.carousel");
});

// Custom Prev Button
$("#customPrevBtn2").click(function () {
  $("#owl-carousel-2").trigger("prev.owl.carousel");
});
$("#customNextBtn3").click(function () {
  $("#owl-carousel-3").trigger("next.owl.carousel");
});

// Custom Prev Button
$("#customPrevBtn3").click(function () {
  $("#owl-carousel-3").trigger("prev.owl.carousel");
});

$(document).ready(function () {
  var maxLegend = 120;

  function metniKisalt(paragraf) {
    if (paragraf.text().length > maxLegend) {
      var kisaltilmisMetin = paragraf.text().slice(0, maxLegend) + "....";
      paragraf.data("original-text", paragraf.text());
      paragraf.text(kisaltilmisMetin);
    }
  }

  function metniGoster(paragraf) {
    var originalText = paragraf.data("original-text");
    paragraf.text(originalText);
  }

  // Sayfa yüklendiğinde çağır
  $(".yorumMetni").each(function () {
    metniKisalt($(this));
  });

  // Daha fazla göster düğmesine tıklanınca çağır
  $(".toggleButton").on("click", function () {
    var paragraf = $(this).prev(".yorumMetni");

    if ($(this).text() === "Daha Fazla Göster") {
      metniGoster(paragraf);
      $(this).text("Daha Az Göster");
    } else {
      metniKisalt(paragraf);
      $(this).text("Daha Fazla Göster");
    }
  });
});

$("#customNextBtn").click(function () {
  owl.trigger("next.owl.carousel");
});

// jQuery ile tıklama olayını yakala
$(document).ready(function () {
  $(".acordion").click(function (e) {
    e.preventDefault();

    // Tıklanan akordeonun içeriğini bul
    var content = $(this).next(".acordion-content");

    // Diğer akordeonların içeriklerini kapat
    $(".acordion-content").not(content).slideUp();

    // Diğer akordeonların "acordion-active" ve "i-active" sınıflarını kaldır
    $(".acordion").not(this).removeClass("acordion-active");
    $(".acordion i").not($(this).find("i")).removeClass("i-active");

    // Tıklanan akordeonun içeriğinin görünürlüğünü değiştir
    content.slideToggle();

    // Tıklanan akordeona "acordion-active" sınıfını ekle/çıkar
    $(this).toggleClass("acordion-active");

    // Tıklanan akordeonun içindeki ikona "i-active" sınıfını ekle/çıkar
    $(this).find("i").toggleClass("i-active");
  });
});

$(".register-alert").hide();
$(document).ready(function () {
  $(".form-register").submit(function (e) {
    e.preventDefault();
    var password1 = $(".password1").val();
    var password2 = $(".password2").val();

    if (password1 === password2) {
      $(".register-alert").hide();
    } else {
      $(".register-alert").show();
    }
  });
});

// login
$(".form-login-mobil").hide();
$(".div-login a").click(function (e) {
  e.preventDefault();

  var dataType = $(this).data("form");

  if (dataType === "mobil") {
    $(".form-login-email").hide();
    $(".form-login-mobil").show();
  } else if (dataType === "eposta") {
    $(".form-login-email").show();
    $(".form-login-mobil").hide();
  }

  $(".div-login a").removeClass("a-active");
  $(this).addClass("a-active");
});

