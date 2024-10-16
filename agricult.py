import streamlit as st

# Set up the page
st.set_page_config(page_title="Agri Products Store", page_icon=":seedling:")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Products", "Cart", "Contact"])

# Simulating a product catalog (you can replace this with a database or file later)
products = [
    {"name": "Organic Wheat", "price": 500, "image": "https://via.placeholder.com/150"},
    {"name": "Fresh Apples", "price": 300, "image": "https://via.placeholder.com/150"},
    {"name": "Organic Rice", "price": 450, "image": "https://via.placeholder.com/150"},
    {"name": "Fresh Oranges", "price": 350, "image": "https://via.placeholder.com/150"}
]

# Initialize session state to store cart information
if 'cart' not in st.session_state:
    st.session_state['cart'] = []

# Home Page
if page == "Home":
    st.title("Welcome to Agri Products Store")
    st.image("https://via.placeholder.com/800x300", caption="Fresh and Organic Products")
    st.write("""
    At Agri Products Store, we offer a wide range of fresh and organic agricultural products.
    Explore our catalog and add your favorite items to the cart. You can place your order online directly.
    """)

# Products Page
elif page == "Products":
    st.title("Our Products")
    
    # Display the product list
    for product in products:
        st.image(product["image"], width=150)
        st.write(f"**{product['name']}**")
        st.write(f"Price: Rs. {product['price']}")
        if st.button(f"Add {product['name']} to cart", key=product['name']):
            st.session_state['cart'].append(product)
            st.success(f"{product['name']} added to cart!")

# Cart Page
elif page == "Cart":
    st.title("Your Cart")
    
    if len(st.session_state['cart']) == 0:
        st.write("Your cart is empty!")
    else:
        total = 0
        for item in st.session_state['cart']:
            st.write(f"**{item['name']}** - Rs. {item['price']}")
            total += item['price']
        st.write(f"**Total: Rs. {total}**")

        if st.button("Place Order"):
            st.write("Order placed! We'll contact you shortly.")

# Contact Page
elif page == "Contact":
    st.title("Contact Us")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message")

        if st.form_submit_button("Submit"):
            st.write("Thank you for reaching out! We'll get back to you soon.")

