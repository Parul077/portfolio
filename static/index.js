function downloadResume() {
  const link = document.createElement("a");
  link.href =
    "https://drive.google.com/file/d/1VOzA5J71FdAFqICWh_SMdyLI0guHz0Fj/view?usp=sharing";
  link.download = "Parul Singh - Resume.pdf";
  link.click();
}

document
  .getElementById("download-btn")
  .addEventListener("click", downloadResume);

// function seeMore() {
//   const seeMoreBtn = document.getElementById("see-more-btn");
//   const hiddenContent = document.getElementById("hidden-content");

//   if (
//     hiddenContent.style.display === "none" ||
//     hiddenContent.style.display === ""
//   ) {
//     hiddenContent.style.display = "block";
//     seeMoreBtn.textContent = "See Less";
//   } else {
//     hiddenContent.style.display = "none";
//     seeMoreBtn.textContent = "See More";
//   }
// }

$(document).ready(function () {
  $("#contactForm").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
      url: '{% url "contact" %}',
      method: "POST",
      data: $(this).serialize(),
      success: function (data) {
        $("#contactForm").hide();
        $("#formSuccess").show();
      },
    });
  });
});
