{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cca4d47a-e24d-439c-bd1c-ef8049e9b412",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tính chu vi và diện tích hình tròn\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Mời bạn nhập bán kính r:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chu vi = 12.57\n",
      "Diện tích = 12.57\n"
     ]
    }
   ],
   "source": [
    "# ex3_circle.py\n",
    "import math\n",
    "print(\"Tính chu vi và diện tích hình tròn\")\n",
    "# Nhập bán kính r (số thực)\n",
    "r = float(input(\"Mời bạn nhập bán kính r: \"))\n",
    "# Tính chu vi và diện tích\n",
    "chu_vi = 2 * math.pi * r\n",
    "dien_tich = math.pi * r**2\n",
    "# In kết quả\n",
    "print(\"Chu vi = %.2f\" % chu_vi)\n",
    "print(\"Diện tích = %.2f\" % dien_tich)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d4c6ffb-2f6e-4c36-bef5-4c47fe975c03",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
