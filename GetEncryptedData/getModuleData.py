{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2ff8640e-77e9-4f69-8e03-e2855e498be5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_module_1_data():\n",
    "    # get the string bytes\n",
    "    line = ''\n",
    "    with open('Texts/text1Encrypted.txt', 'rb') as file:\n",
    "        line = file.readlines()[0]\n",
    "    \n",
    "    video_data = list()\n",
    "    with open('videos/encryptedVideos/encryptedVideo1.mp4', 'rb') as file:\n",
    "        video_data = file.read()\n",
    "    return (line, video_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ea928b9d-9f72-40e0-ab2f-cc0690c0c25a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_module_2_data():\n",
    "    # get the string bytes\n",
    "    line = ''\n",
    "    with open('Texts/text2Encrypted.txt', 'rb') as file:\n",
    "        line = file.readlines()[0]\n",
    "    \n",
    "    video_data = list()\n",
    "    with open('videos/encryptedVideos/encryptedVideo2.mp4', 'rb') as file:\n",
    "        video_data = file.read()\n",
    "    return (line, video_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "80ac7e98-fee3-4017-8337-ed83d958d0a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_module_3_data():\n",
    "    # get the string bytes\n",
    "    line = ''\n",
    "    with open('Texts/text3Encrypted.txt', 'rb') as file:\n",
    "        line = file.readlines()[0]\n",
    "    \n",
    "    video_data = list()\n",
    "    with open('videos/encryptedVideos/encryptedVideo3.mp4', 'rb') as file:\n",
    "        video_data = file.read()\n",
    "    return (line, video_data)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "SageMath 9.5",
   "language": "sage",
   "name": "sagemath"
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
