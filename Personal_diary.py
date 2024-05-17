{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMoHfw/fqA63jxYmG/j5cHI",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Aruna168/Personal-diary/blob/main/Personal_diary.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def login(password):\n",
        "    stored_password = \"password123\"  # Predefined password\n",
        "    if password == stored_password:\n",
        "        return True\n",
        "    else:\n",
        "        print(\"Incorrect password.\")\n",
        "        return False\n",
        "def write_entry():\n",
        "    entry = input(\"Write your diary entry: \")\n",
        "    with open(\"diary.txt\", \"a\") as file:\n",
        "        file.write(entry + \"\\n\")\n",
        "def read_entries():\n",
        "    with open(\"diary.txt\", \"r\") as file:\n",
        "       entries = file.readlines()\n",
        "       for entry in entries:\n",
        "           print(entry.strip())\n",
        "def main():\n",
        "    password = input(\"Enter password: \")\n",
        "    if login(password):\n",
        "        while True:\n",
        "            print(\"\\n1. Write Diary Entry\")\n",
        "            print(\"2. Read Diary Entries\")\n",
        "            print(\"3. Exit\")\n",
        "            choice = input(\"Enter your choice: \")\n",
        "            if choice == \"1\":\n",
        "                write_entry()\n",
        "            elif choice == \"2\":\n",
        "                read_entries()\n",
        "            elif choice == \"3\":\n",
        "                print(\"Exiting program.\")\n",
        "                break\n",
        "            else:\n",
        "                print(\"Invalid choice.\")\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XfBxN48j8zlG",
        "outputId": "e013bd4f-733a-4117-ab68-f99f2ee51a7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter password: password123\n",
            "\n",
            "1. Write Diary Entry\n",
            "2. Read Diary Entries\n",
            "3. Exit\n",
            "Enter your choice: 1\n",
            "Write your diary entry: helloworld\n",
            "\n",
            "1. Write Diary Entry\n",
            "2. Read Diary Entries\n",
            "3. Exit\n",
            "Enter your choice: 2\n",
            "helloworld\n",
            "\n",
            "1. Write Diary Entry\n",
            "2. Read Diary Entries\n",
            "3. Exit\n",
            "Enter your choice: 3\n",
            "Exiting program.\n"
          ]
        }
      ]
    }
  ]
}