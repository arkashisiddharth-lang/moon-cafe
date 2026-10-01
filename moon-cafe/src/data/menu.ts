export type Category = "Coffee" | "Cold Drinks" | "Tea" | "Bakery" | "Desserts";

export type MenuItem = {
  id: string;
  name: string;
  description: string;
  price: number;
  category: Category;
  image: string;
};

export const categories: { name: Category; blurb: string; note: string }[] = [
  { name: "Coffee", blurb: "Poured slowly, steamed to order, served warm.", note: "Oat, almond or soy milk on request." },
  { name: "Cold Drinks", blurb: "Chilled, layered and made for warm evenings.", note: "Ask for less sweet — we're happy to adjust." },
  { name: "Tea", blurb: "Whole-leaf and spiced teas, brewed by the pot.", note: "Every cup comes with a small jug of honey." },
  { name: "Bakery", blurb: "Baked each morning and warmed before it reaches you.", note: "Fresh batches land on the counter by 8 AM." },
  { name: "Desserts", blurb: "Made in small batches for the late hours.", note: "Sharing plates available — just ask for two spoons." },
];

const img = (n: string) => `/images/${n}.svg`;

export const menu: MenuItem[] = [
  { id: "moon-latte", name: "Moon Latte", description: "Double espresso, silky steamed milk and a hand-poured crescent.", price: 220, category: "Coffee", image: img("moon-latte") },
  { id: "caramel-cappuccino", name: "Caramel Cappuccino", description: "Thick velvety foam over espresso, finished with house caramel.", price: 230, category: "Coffee", image: img("caramel-cappuccino") },
  { id: "dark-chocolate-mocha", name: "Dark Chocolate Mocha", description: "Espresso melted into 70% dark chocolate and steamed milk.", price: 260, category: "Coffee", image: img("dark-mocha") },
  { id: "flat-white", name: "Flat White", description: "A ristretto double with a thin, glossy layer of microfoam.", price: 210, category: "Coffee", image: img("flat-white") },
  { id: "espresso-doppio", name: "Espresso Doppio", description: "Two shots, short and syrupy, with a caramel crema.", price: 150, category: "Coffee", image: img("espresso-doppio") },

  { id: "midnight-cold-brew", name: "Midnight Cold Brew", description: "Steeped for eighteen hours, served over ice and very smooth.", price: 240, category: "Cold Drinks", image: img("midnight-cold-brew") },
  { id: "iced-spanish-latte", name: "Iced Spanish Latte", description: "Espresso, milk and condensed milk, poured in layers over ice.", price: 250, category: "Cold Drinks", image: img("iced-spanish-latte") },
  { id: "salted-caramel-frappe", name: "Salted Caramel Frappé", description: "Blended coffee, salted caramel and cream, topped with cocoa.", price: 270, category: "Cold Drinks", image: img("salted-caramel-frappe") },
  { id: "lemon-mint-cooler", name: "Lemon Mint Cooler", description: "Fresh lemon, crushed mint and soda. Bright and caffeine-free.", price: 190, category: "Cold Drinks", image: img("lemon-mint-cooler") },

  { id: "masala-chai", name: "Masala Chai", description: "Assam leaf simmered with ginger, cardamom and whole spices.", price: 140, category: "Tea", image: img("masala-chai") },
  { id: "jasmine-green-tea", name: "Jasmine Green Tea", description: "Green tea scented with jasmine blossom. Light and floral.", price: 180, category: "Tea", image: img("jasmine-green-tea") },
  { id: "earl-grey", name: "Earl Grey with Lemon", description: "Bergamot black tea served with a thin slice of lemon.", price: 170, category: "Tea", image: img("earl-grey") },
  { id: "saffron-moon-milk", name: "Saffron Moon Milk", description: "Warm milk with saffron, cardamom and a little honey.", price: 200, category: "Tea", image: img("saffron-moon-milk") },

  { id: "butter-croissant", name: "Butter Croissant", description: "Laminated by hand, crisp outside, soft and layered inside.", price: 180, category: "Bakery", image: img("butter-croissant") },
  { id: "almond-croissant", name: "Almond Croissant", description: "Filled with almond cream and finished with toasted flakes.", price: 210, category: "Bakery", image: img("almond-croissant") },
  { id: "blueberry-muffin", name: "Blueberry Muffin", description: "Tender crumb, a sugar crust and plenty of blueberries.", price: 160, category: "Bakery", image: img("blueberry-muffin") },
  { id: "sourdough-toast", name: "Sourdough Butter Toast", description: "Thick-cut sourdough, grilled and served with cultured butter.", price: 220, category: "Bakery", image: img("sourdough-toast") },

  { id: "classic-tiramisu", name: "Classic Tiramisu", description: "Espresso-soaked ladyfingers, mascarpone cream and cocoa.", price: 280, category: "Desserts", image: img("classic-tiramisu") },
  { id: "basque-cheesecake", name: "Basque Cheesecake", description: "Burnt on top, creamy in the middle, served with berries.", price: 300, category: "Desserts", image: img("basque-cheesecake") },
  { id: "warm-brownie", name: "Warm Brownie", description: "Fudgy dark chocolate brownie with a scoop of vanilla ice cream.", price: 250, category: "Desserts", image: img("warm-brownie") },
  { id: "panna-cotta", name: "Berry Panna Cotta", description: "Vanilla cream set softly and topped with a warm berry sauce.", price: 260, category: "Desserts", image: img("panna-cotta") },
];

export const formatPrice = (n: number) => `₹${n}`;
