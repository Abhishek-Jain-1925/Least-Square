from utils.libraries import *


def show_explore_page(cars):

    st.write(
        """
        # Welcome to My Cars24.com

## Featured Cars

### Toyota Camry
![Toyota Camry]([https://example.com/toyota-camry.jpg](https://cdni.autocarindia.com/utils/imageresizer.ashx?n=https://cms.haymarketindia.net/model/uploads/modelimages/CamryModelImage.jpg))
- **Year:** 2020
- **Price:** Rs.20,000
- **KM Driven:** 30,000 km

### Honda Civic
![Honda Civic]([https://example.com/honda-civic.jpg](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.carwale.com%2Fhonda-cars%2Fcivic%2F&psig=AOvVaw3iwlz6dP6pQB8zEAm-Yroa&ust=1695806819490000&source=images&cd=vfe&opi=89978449&ved=0CA4QjRxqFwoTCLjq9uv6x4EDFQAAAAAdAAAAABAD))
- **Year:** 2019
- **Price:** Rs.18,500
- **KM Driven:** 35,000 km

### Tata Altroz
![Tata Altroz]([https://example.com/honda-civic.jpg](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.carwale.com%2Fhonda-cars%2Fcivic%2F&psig=AOvVaw3iwlz6dP6pQB8zEAm-Yroa&ust=1695806819490000&source=images&cd=vfe&opi=89978449&ved=0CA4QjRxqFwoTCLjq9uv6x4EDFQAAAAAdAAAAABAD))]
- **Year:** 2023
- **Price:** Rs.9,00,000
- **KM Driven:** 10,000 km

## Search for Cars

Use the form below to search for cars:



### About Us

We are a trusted car dealership dedicated to helping you find the perfect vehicle.

Contact us at [jainabhishek1925@gmail.com](mailto:jainabhishek1925@gmail.com).

---

**Disclaimer:** This is a simplified example and does not replicate the functionality or complexity of a website like Cars24.com. To create a website like Cars24.com, you would need to use web development technologies such as HTML, CSS, JavaScript, and potentially backend languages and databases to manage car listings and user interactions. Markdown is not suitable for creating fully functional web applications.


        """
    )

    st.title("Explore Cars Dataset")

    st.write(
        """
    ### Cars
    """
    )
    st.dataframe(cars.head())

    shape = cars.shape
    st.write("There are", shape[0], "rows and ", shape[1], "columns in the Dataset.")

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (8, 5)})
    plt.title("Heat Map for Missing Values")
    sns.heatmap(cars.isnull(), yticklabels=False, cbar=False, cmap='viridis')
    st.pyplot(fig)

    cars.dropna(inplace=True)

    st.write("""
        #### Exploratory Data Analysis
        """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Countplot Owner Type Vs Number of Cars")
    sns.countplot(x ='Owner_Type', data = cars)
    st.pyplot(fig)

    st.write("""
        **Observation**

        **First Owned Cars** are **highest among all**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Type of Owner Vs Number of cars")
    plt.pie(cars['Owner_Type'].value_counts(),labels=cars['Owner_Type'].unique(),pctdistance=1.1, labeldistance=1.2,autopct='%.2f')
    st.pyplot(fig)

    st.write("""
        **Observation**

        1. **79.75 %** of cars are **First Owned**.
        2. **19.46 %** of cars are **Second Owned**.
        3. **0.79 %** of cars are **Third Owned**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Owner Type Vs Price")
    sns.barplot(x='Owner_Type',y='Price',data=cars,palette='spring')
    st.pyplot(fig)

    st.write("""
        **Observation**

        **First Owner cars** have **high average selling price**. 

        As **number of owners** increases the **selling price** of car **decreases**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Transmission Vs Number of Cars")
    sns.countplot(x ='Transmission', data = cars)
    st.pyplot(fig)

    st.write("""
        **Observation**

        Most of the cars are **Manual**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Transmission Vs Selling Price")
    sns.barplot(x='Transmission',y='Price',data=cars,palette='spring')
    st.pyplot(fig)

    st.write("""
        **Observation**

        Cars having **Automatic Transmission have high selling price**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Fuel Vs Number of Cars")
    sns.countplot(x ='Fuel', data = cars)
    st.pyplot(fig)

    st.write("""
        **Observation**

        Most of the cars are **Petrol**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Fuel Vs Price")
    sns.barplot(x='Fuel',y='Price',data=cars,palette='spring')
    st.pyplot(fig)

    st.write("""
        **Observation**

        **Diesel cars** have **high average selling price**.
    """)

    fig, ax = plt.subplots()
    ax = sns.set(rc={'figure.figsize': (10, 8)})
    plt.title("Fuel Vs Selling Price")
    sns.barplot(x ='Age', y="Price", data = cars ,palette='spring')
    st.pyplot(fig)

    st.write("""
        **Observation**

        As the age of Vehical increases, Price Decreases.
    """)
