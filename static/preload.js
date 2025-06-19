// On page load or when changing themes, best to add inline in `head` to avoid
document.documentElement.classList.toggle(
  "dark",
  localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches),
);

// load functions
function toggleDarkMode() {
  if (localStorage.theme === "dark") {
    document.documentElement.classList.remove("dark");
    localStorage.theme = "light";
  } else if (localStorage.theme === "light") {
    document.documentElement.classList.add("dark");
    localStorage.theme = "dark";
  }
}

function toggleModal() {
  document.getElementById("content-block").classList.toggle("blur-sm");
  document.getElementById("modal").classList.toggle("hidden");
  //document.getElementById('popup').classList.toggle('hidden');
}
