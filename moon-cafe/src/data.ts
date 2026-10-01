export const links = [['Home','/'],['Menu','/menu'],['About','/about'],['Experience','/experience'],['Gallery','/gallery'],['Reviews','/reviews'],['Contact','/contact']] as const
export const cats = ['Coffee','Cold Drinks','Tea','Bakery','Desserts'] as const
export type Item = { cat: typeof cats[number]; name: string; desc: string; price: number; tone: number }
export const menu: Item[] = [
 {cat:'Coffee',name:'Moon Latte',desc:'Double espresso, steamed milk, a whisper of vanilla and honey.',price:220,tone:0},
 {cat:'Coffee',name:'Caramel Cappuccino',desc:'Velvet foam over slow-cooked caramel.',price:230,tone:1},
 {cat:'Coffee',name:'Dark Chocolate Mocha',desc:'70% cocoa melted into a bold espresso base.',price:260,tone:2},
 {cat:'Cold Drinks',name:'Midnight Cold Brew',desc:'Steeped 18 hours, served over one large ice sphere.',price:240,tone:3},
 {cat:'Cold Drinks',name:'Iced Orange Espresso',desc:'Espresso, fresh orange, sparkling water.',price:250,tone:1},
 {cat:'Cold Drinks',name:'Cardamom Frappe',desc:'Blended coffee with green cardamom and cream.',price:270,tone:4},
 {cat:'Tea',name:'Masala Chai',desc:'Assam leaves simmered with ginger and spice.',price:160,tone:2},
 {cat:'Tea',name:'Jasmine Pearl',desc:'Hand-rolled green tea, floral and soft.',price:190,tone:4},
 {cat:'Tea',name:'Earl Grey Cream',desc:'Bergamot black tea finished with warm milk.',price:180,tone:0},
 {cat:'Bakery',name:'Butter Croissant',desc:'Laminated for 27 layers, baked every morning.',price:180,tone:1},
 {cat:'Bakery',name:'Almond Danish',desc:'Frangipane, toasted almonds, apricot glaze.',price:200,tone:3},
 {cat:'Bakery',name:'Sourdough Toastie',desc:'Cheddar, caramelised onion, thyme butter.',price:240,tone:2},
 {cat:'Desserts',name:'Classic Tiramisu',desc:'Mascarpone, espresso-soaked sponge, cocoa dust.',price:280,tone:0},
 {cat:'Desserts',name:'Molten Lava Cake',desc:'Warm dark chocolate centre with vanilla cream.',price:290,tone:3},
 {cat:'Desserts',name:'Salted Caramel Tart',desc:'Buttery shortcrust, sea salt, gold leaf.',price:260,tone:4}]
export const reviews = [
 ['Beautiful atmosphere, amazing coffee and the perfect place to spend an evening.','Aarav'],
 ['One of those cafés where you want to stay longer than planned.','Meera'],
 ['The cold brew is dangerous. I now plan my week around it.','Kabir'],
 ['Quiet corners, warm light, and a tiramisu that deserves its own fan club.','Ishita']] as const
