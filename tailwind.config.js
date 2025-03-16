/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./node_modules/flyonui/dist/js/*.js", // Require only if you want to use FlyonUI JS component
  ],

  flyonui: {
    themes: ["soft", "dark", "gourmet", "light"],
  },

  theme: {
    extend: {},
  },
  plugins: [
    require("flyonui"),
    require("flyonui/plugin"), // Require only if you want to use FlyonUI JS component
  ],
};
