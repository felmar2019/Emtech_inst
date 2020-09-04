#!/usr/bin/env python
# coding: utf-8

# In[13]:


from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches


# In[17]:


lifestore_searches_names = ['id_search', 'id_product']
lifestore_sales_names = ['id_sale', 'id_product', 'score', 'date', 'refund']
lifestore_products_names = ['id_product', 'name', 'price', 'category', 'stock']

print(f"Cantidad de productos: {len(lifestore_products)}")
print(f"Cantidad de ventas: {len(lifestore_sales)}")
print(f"Cantidad de búsquedas: {len(lifestore_searches)}")


# In[ ]:





# In[ ]:




