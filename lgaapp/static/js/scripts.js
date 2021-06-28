function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function makeRequest(url, method, csrftoken) {
  return fetch(url, {
    method: method,
    mode: "same-origin",
    headers: { "X-CSRFToken": csrftoken },
  });
}

function confirmDelete(book_name, book_pk) {
  let del = confirm(
    'Ви видаляєте книгу "' + book_name + '" з бібліотеки.\n\nВсе правильно?'
  );
  if (del === true) {
    const csrftoken = getCookie("csrftoken");

    makeRequest("/about/" + book_pk + "/", "DELETE", csrftoken);

    window.location.href = "/"; // redirect to Home page
  }
}
