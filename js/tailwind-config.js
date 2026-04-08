/**
 * WonderBees Services — brand theme (Roboto / Roboto Slab, purple + sky + sage + cream)
 */
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#6A5EA9",
          foreground: "#FFFFFF",
          hover: "#5A4F94",
          active: "#4C4380",
        },
        secondary: {
          DEFAULT: "#62ACDF",
          foreground: "#FFFFFF",
          hover: "#4B9AD6",
          muted: "#8BC0E8",
        },
        accent: {
          DEFAULT: "#99C2A2",
          foreground: "#191B41",
          hover: "#7EAE89",
          active: "#6A9A75",
        },
        base: {
          DEFAULT: "#FFFFFF",
          alt: "#F5EFE6",
        },
        muted: {
          DEFAULT: "#5E5E5E",
          foreground: "#FFFFFF",
          subtle: "#7A7A7A",
        },
        surface: {
          DEFAULT: "#FFFFFF",
          elevated: "#FFFFFF",
          border: "#DDD5C8",
        },

        cream: "#E7D7C1",
        sand: "#F5EFE6",
        paper: "#FFFFFF",
        ink: "#191B41",
        line: "#DDD5C8",

        nn: {
          white: "#FFFFFF",
          secondary: "#191B41",
          body: "#3F3F3F",
          wash: "#DDD5C8",
          link: "#6A5EA9",
          sage: "#99C2A2",
          teal: "#62ACDF",
          "teal-light": "#7EBEE8",
          pink: "#5A4F94",
          "pink-soft": "#62ACDF",
          creamline: "#DDD5C8",
          page: "#FFFFFF",
          surface: "#FFFFFF",
          elevated: "#FFFFFF",
          blush: "#F5EFE6",
          sagebg: "#99C2A2",
          line: "#7A7A7A",
          cta: "#6A5EA9",
          "cta-deep": "#5A4F94",
        },
      },
      fontFamily: {
        sans: ['"Roboto"', "system-ui", "Segoe UI", "sans-serif"],
        display: ['"Roboto Slab"', "Georgia", "serif"],
      },
      fontSize: {
        "nn-h1": ["2.8em", { lineHeight: "1.1", letterSpacing: "-0.03em", fontWeight: "600" }],
        "nn-h2": ["2em", { lineHeight: "1.35", fontWeight: "600" }],
        "nn-h4": ["1.3em", { lineHeight: "1.4", letterSpacing: "-0.01em", fontWeight: "500" }],
        "nn-body": ["18px", { lineHeight: "1.75" }],
        "nn-small": ["16px", { lineHeight: "1.6", fontWeight: "500" }],
      },
      maxWidth: {
        nn: "1140px",
        "nn-wide": "1400px",
      },
      boxShadow: {
        nn: "0px 20px 50px rgba(25, 27, 65, 0.08)",
        "nn-lg": "0px 28px 60px rgba(25, 27, 65, 0.1)",
        "nn-card": "0px 8px 28px rgba(25, 27, 65, 0.08)",
        "nn-review": "0 12px 32px rgba(25, 27, 65, 0.09)",
      },
      backgroundImage: {
        "hero-gradient":
          "linear-gradient(165deg, #FFFFFF 0%, #F3F0FA 38%, #EDE4F7 65%, #E7D7C1 100%)",
        "nn-flowers":
          "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'%3E%3Ccircle cx='10' cy='12' r='3' fill='%236A5EA9' fill-opacity='.07'/%3E%3Ccircle cx='38' cy='40' r='4' fill='%2362ACDF' fill-opacity='.08'/%3E%3C/svg%3E\")",
      },
      borderRadius: {
        nn: "10px",
        "nn-lg": "15px",
        "nn-xl": "20px",
        "nn-2xl": "25px",
      },
      transitionDuration: {
        400: "400ms",
      },
    },
  },
};
