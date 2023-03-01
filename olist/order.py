import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist
olist = Olist()
data = olist.get_data()
orders = data['orders'].copy() # good practice to be sure not to modify your `data` variable
assert(orders.shape == (99441, 8))


class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()


    def get_wait_time(self, is_delivered=True):
        """
        Returns the wait time for a given order status.
        """
        delivered_orders = orders[orders.order_status == 'delivered'].copy()
        delivered_orders.loc[:, 'order_purchase_timestamp'] = delivered_orders.loc[:, 'order_purchase_timestamp'].apply(pd.to_datetime)
        delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]] = delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]].apply(pd.to_datetime)
        #convert dates from "string" type to "pandas.datetime' using pandas.to_datetime()
        delivered_orders.loc[:, 'order_purchase_timestamp'] = delivered_orders.loc[:, 'order_purchase_timestamp'].apply(pd.to_datetime)
        delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]] = delivered_orders.loc[:,['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date','order_delivered_customer_date', 'order_estimated_delivery_date', ]].apply(pd.to_datetime)
        # add wait_time column
        delivered_orders.loc[:, 'wait_time'] = delivered_orders.order_delivered_customer_date - delivered_orders.order_purchase_timestamp
        # Compute expected_wait_time using loc
        delivered_orders.loc[:, 'expected_wait_time'] = delivered_orders.order_estimated_delivery_date - delivered_orders.order_purchase_timestamp
        # Compute delay_vs_expected
        delivered_orders.loc[:, 'delay_vs_expected'] = delivered_orders.order_delivered_customer_date - delivered_orders.order_estimated_delivery_date
        #show only order_id, wait_time, expected_wait_time, delay_vs_expected, order_status
        delivered_orders = delivered_orders[['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected', 'order_status']]

        return delivered_orders

    def get_review_score(self):
        """
        Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        pass  # YOUR CODE HERE

    def get_number_products(self):
        """
        Returns a DataFrame with:
        order_id, number_of_products
        """
        pass  # YOUR CODE HERE

    def get_number_sellers(self):
        """
        Returns a DataFrame with:
        order_id, number_of_sellers
        """
        pass  # YOUR CODE HERE

    def get_price_and_freight(self):
        """
        Returns a DataFrame with:
        order_id, price, freight_value
        """
        pass  # YOUR CODE HERE

    # Optional
    def get_distance_seller_customer(self):
        """
        Returns a DataFrame with:
        order_id, distance_seller_customer
        """
        pass  # YOUR CODE HERE

    def get_training_data(self,
                          is_delivered=True,
                          with_distance_seller_customer=False):
        """
        Returns a clean DataFrame (without NaN), with the all following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_products', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """
        # Hint: make sure to re-use your instance methods defined above
        pass  # YOUR CODE HERE
