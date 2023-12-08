import streamlit as st
import pandas as pd

def st_button(url, label, font_awesome_icon):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    button_code = f'''<a href="{url}" target=_blank><i class="fa {font_awesome_icon}"></i>   {label}</a>'''
    return st.markdown(button_code, unsafe_allow_html=True)

def main():
    st.title("Brand Equity Estimates")

    # Add custom CSS styles to adjust the size of the sidebar and buttons
    st.markdown(
        """
        <style>
            .sidebar .css-145kmo2 {
                width: 500px;
            }
            .sidebar button {
                width: 150px;
                padding: 10px;
                margin: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add a selectbox for tab selection
    selected_tab = st.sidebar.selectbox("Select a tab", ["Effect of environmental footprint on brand equity",
     "Components of brand equity", "Components of environmental footprint", "Mediating effects"])


## Tab 1
    # Display the content of the selected tab
    if selected_tab == "Effect of environmental footprint on brand equity":
        selected_value = st.selectbox('Moderator', [None, "No moderator", "CSR reputation", "Media attention", "Societal trust in business", "All three moderators"])

        if selected_value == 'None':
            st.text('Please select a value from the dropdown.')
        elif selected_value == "No moderator":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Effect of environmental footprint': ['-1.041 (0.315) ***'],
            'Moderating effect 1': ['-'],
            'Moderating effect 2': ['-'],
            'Moderating effect 3': ['-']}

            # Define the row labels for the dataframe
            index = ['No moderator']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "CSR reputation":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Effect of environmental footprint': ['-1.286 (0.345) ***'],
            'Moderating effect 1': ['-0.0305 (0.0119) **'],
            'Moderating effect 2': ['-'],
            'Moderating effect 3': ['-']}

            # Define the row labels for the dataframe
            index = ['CSR reputation']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "Media attention":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Effect of environmental footprint': ['-1.043 (0.324) ***'],
            'Moderating effect 1': ['0.00138 (0.0133)'],
            'Moderating effect 2': ['-'],
            'Moderating effect 3': ['-']}

            # Define the row labels for the dataframe
            index = ['Media attention']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "Societal trust in business":
            st.write(f"Showing data for: {selected_value}")
            data = {
            'Effect of environmental footprint': ['-0.734 (0.295) **'],
            'Moderating effect 1': ['-0.0329 (0.0133) **'],
            'Moderating effect 2': ['-'],
            'Moderating effect 3': ['-']}

            # Define the row labels for the dataframe
            index = ['Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "All three moderators":
            st.write(f"Showing data for: {selected_value}")

            data = {
            'Effect of environmental footprint': ['-0.961 (0.319) ***'],
            'Moderating effect 1': ['-0.0333 (0.0124) ***'],
            'Moderating effect 2': ['-0.0109 (0.0151)'],
            'Moderating effect 3': ['-0.0351 (0.0127) ***']}

            # Define the row labels for the dataframe
            index = ['All three moderators']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)


## Tab 2
    elif selected_tab == "Components of brand equity":

        selected_value = st.selectbox('Component of brand equity ', [None, "Brand stature", "Brand strength"])

        if selected_value == 'None':
            st.text('Please select a value from the dropdown.')

        elif selected_value == 'Brand stature':
            st.write(f"Showing data for: {selected_value}")

            data = {
            'Brand stature': ['-1.377*** (0.384)', '-0.0287** (0.0119)', '-0.00492 (0.0151)', '-0.0224* (0.0133)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)


        elif selected_value == 'Brand strength':
            st.write(f"Showing data for: {selected_value}")

            data = {
            'Brand stature': ['-0.204 (0.278)', '-0.0296** (0.0135)', '-0.0252 (0.0186)', '-0.0296 (0.0186)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

## Tab 3
    elif selected_tab == "Components of environmental footprint":
        selected_value = st.selectbox("Components of environmental footprint", [None, "Land and water pollution",
        "Air pollution + GHG emissions", "Waste", "Water use", "Other natural resource use"])

        if selected_value == 'None':
            st.text('Please select a value from the dropdown.')
        elif selected_value == "Land and water pollution":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Land and water pollution': ['-0.0934** (0.0445)', '-0.0130** (0.00526)', '-0.000765 (0.00581)', '-0.0111 (0.00706)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "Air pollution + GHG emissions":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Air pollution + GHG emissions': ['0.188 (3.615)', '-0.0187 (0.0144)', '-0.00931 (0.0233)', '-0.0338** (0.0140)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "Waste":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Waste': ['4.502 (6.564)', '0.0290 (0.0417)', '0.0101 (0.0572)', '-0.0145 (0.0191)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "Water use":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Water use': ['-1.279*** (0.108)', '-0.0207** (0.00808)', '-0.00983 (0.0123)', '-0.0191* (0.0112)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value == "Other natural resource use":
            st.write(f"Showing data for: {selected_value}")
            # Define the data for the datafram
            data = {
            'Other natural resource use': ['2.278 (3.613)', '-0.143 (0.204)', '0.0418 (0.223)', '-0.174 (0.174)']}

            # Define the row labels for the dataframe
            index = ['Environmental footprint', 'Environmental footprint × CSR reputation',
            'Environmental footprint × Media attention', 'Environmental footprint × Societal trust in business']

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

## tab 4
    elif selected_tab == "Mediating effects":
        selected_value_first = st.selectbox("Mediating variable", ["Brand equity", "Brand stature"])
        selected_value_second = st.selectbox("Performance variable", [None, "Accounting", "Financial"])

        if selected_value_first == "Brand equity" and selected_value_second is None:
            st.write(f"Showing data for: {selected_value_first}")

            data = {
            'Effect of environmental footprint on mediating variable': ['-1.041 (0.514) **']}

            # Define the row labels for the dataframe
            index = ["Brand equity"]

            df = pd.DataFrame(data = data, index = index)
            st.table(df)


        elif selected_value_first == "Brand stature" and selected_value_second is None:
            st.write(f"Showing data for: {selected_value_first}")

            data = {
            'Effect of environmental footprint on mediating variable': ['-1.365 (0.538) **']}

            # Define the row labels for the dataframe
            index = ["Brand stature"]

            df = pd.DataFrame(data = data, index = index)
            st.table(df)

        elif selected_value_first == "Brand equity" and selected_value_second == "Accounting":
            st.write(f"Showing data for: {selected_value_first} and {selected_value_second}")

            data = {'Mediating variable': ['Brand equity'],
            'Performance ': ['Accounting'],
            'Effect': ['0.108 (0.0283) ***']}

            df = pd.DataFrame(data = data)
            st.table(df)

        elif selected_value_first == "Brand stature" and selected_value_second == "Accounting":
            st.write(f"Showing data for: {selected_value_first} and {selected_value_second}")

            data = {'Mediating variable': ['Brand stature'],
            'Performance ': ['Accounting'],
            'Effect': ['0.124 (0.0304) ***']}

            df = pd.DataFrame(data = data)
            st.table(df)

        elif selected_value_first == "Brand equity" and selected_value_second == "Financial":
            st.write(f"Showing data for: {selected_value_first} and {selected_value_second}")

            data = {'Mediating variable': ['Brand equity'],
            'Performance ': ['Financial'],
            'Effect': ['0.0490 (0.0159) ***']}

            df = pd.DataFrame(data = data)
            st.table(df)

        elif selected_value_first == "Brand stature" and selected_value_second == "Financial":
            st.write(f"Showing data for: {selected_value_first} and {selected_value_second}")

            data = {'Mediating variable': ['Brand stature'],
            'Performance ': ['Financial'],
            'Effect': ['0.0556 (0.0160) ***']}

            df = pd.DataFrame(data = data)
            st.table(df)




if __name__ == "__main__":
    main()
