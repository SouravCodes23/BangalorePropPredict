// ✅ Set your Render backend base URL here
var baseURL = "https://bangaloreproppredict-3.onrender.com";

function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");

  var sqft = parseFloat(document.getElementById("uiSqft").value);
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations").value;
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = baseURL + "/predict_home_price";

  // ✅ Use JSON body instead of form POST
  $.ajax({
    url: url,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      total_sqft: sqft,
      bhk: bhk,
      bath: bathrooms,
      location: location
    }),
    success: function (data) {
      console.log("Prediction response:", data);
      if (data && data.estimated_price) {
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      } else {
        estPrice.innerHTML = "<h2>No price returned</h2>";
      }
    },
    error: function (xhr, status, error) {
      console.error("Error:", status, error, xhr.responseText);
      estPrice.innerHTML = "<h2>Error calculating price</h2>";
    }
  });
}

function onPageLoad() {
  console.log("document loaded");

  var url = baseURL + "/get_location_names";

  // ✅ Simpler GET request
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data && data.locations) {
      $('#uiLocations').empty();
      for (var i in data.locations) {
        $('#uiLocations').append(new Option(data.locations[i]));
      }
    }
  }).fail(function (xhr, status, error) {
    console.error("Error fetching locations:", status, error, xhr.responseText);
  });
}

window.onload = onPageLoad;
