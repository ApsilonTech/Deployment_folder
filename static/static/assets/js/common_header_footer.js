// common.js
function loadHeader() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/header', true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      document.getElementById('headerPart').innerHTML = xhr.responseText;
    }
  };
  xhr.send();
}

function loadFooter() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/footer', true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      document.getElementById('footerPart').innerHTML = xhr.responseText;
    }
  };
  xhr.send();
}

document.addEventListener('DOMContentLoaded', function () {
  loadHeader();
  loadFooter();
});
