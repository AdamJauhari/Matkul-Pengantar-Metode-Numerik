{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPQgUMvyyT4UAc41vhdyTQN",
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
        "<a href=\"https://colab.research.google.com/github/AdamJauhari/Matkul-Pengantar-Metode-Numerik/blob/main/SPL.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C4YvWD6k2iNi",
        "outputId": "8e32b5be-1215-4eb7-a547-ecea3e0fda12"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan jumlah persamaan: 3\n",
            "Masukkan koefisien dan konstanta setiap persamaan (dipisahkan spasi):\n",
            "6 9 32 4\n",
            "9 64 32 2\n",
            "100 12 34 5\n",
            "Solusi:\n",
            "x1 = 0.01\n",
            "x2 = -0.04\n",
            "x3 = 0.13\n"
          ]
        }
      ],
      "source": [
        "def gauss_jordan_solve(matrix):\n",
        "    matrix = [row.copy() for row in matrix]\n",
        "    rows = len(matrix)\n",
        "    if rows == 0:\n",
        "        return []\n",
        "    cols = len(matrix[0])\n",
        "    if cols == 0:\n",
        "        return []\n",
        "    pivot_row = 0\n",
        "\n",
        "    for pivot_col in range(cols - 1):\n",
        "        max_row = pivot_row\n",
        "        for r in range(pivot_row, rows):\n",
        "            if abs(matrix[r][pivot_col]) > abs(matrix[max_row][pivot_col]):\n",
        "                max_row = r\n",
        "\n",
        "        if abs(matrix[max_row][pivot_col]) < 1e-10:\n",
        "            continue\n",
        "\n",
        "        matrix[pivot_row], matrix[max_row] = matrix[max_row], matrix[pivot_row]\n",
        "\n",
        "        pivot_val = matrix[pivot_row][pivot_col]\n",
        "        matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]\n",
        "\n",
        "        for r in range(rows):\n",
        "            if r != pivot_row:\n",
        "                factor = matrix[r][pivot_col]\n",
        "                matrix[r] = [matrix[r][i] - factor * matrix[pivot_row][i] for i in range(cols)]\n",
        "\n",
        "        pivot_row += 1\n",
        "\n",
        "    for r in range(rows):\n",
        "        if all(abs(x) < 1e-10 for x in matrix[r][:-1]) and abs(matrix[r][-1]) > 1e-10:\n",
        "            return \"Tidak ada solusi.\"\n",
        "\n",
        "    leading_cols = []\n",
        "    for r in range(rows):\n",
        "        for c in range(cols - 1):\n",
        "            if abs(matrix[r][c] - 1) < 1e-10:\n",
        "                valid = True\n",
        "                for r2 in range(rows):\n",
        "                    if r2 != r and abs(matrix[r2][c]) > 1e-10:\n",
        "                        valid = False\n",
        "                        break\n",
        "                if valid:\n",
        "                    leading_cols.append(c)\n",
        "                break\n",
        "\n",
        "    if len(leading_cols) < cols - 1:\n",
        "        return \"Ada solusi tak hingga banyak.\"\n",
        "    else:\n",
        "        solution = [0.0] * (cols - 1)\n",
        "        for r in range(rows):\n",
        "            for c in range(cols - 1):\n",
        "                if abs(matrix[r][c] - 1) < 1e-10:\n",
        "                    solution[c] = matrix[r][-1]\n",
        "                    break\n",
        "        return solution\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    n = int(input(\"Masukkan jumlah persamaan: \"))\n",
        "    print(\"Masukkan koefisien dan konstanta setiap persamaan (dipisahkan spasi):\")\n",
        "    matrix = []\n",
        "    for _ in range(n):\n",
        "        row = list(map(float, input().split()))\n",
        "        if len(row) != n + 1:\n",
        "            print(\"Error: Setiap persamaan harus memiliki n koefisien dan 1 konstanta.\")\n",
        "            exit()\n",
        "        matrix.append(row)\n",
        "    result = gauss_jordan_solve(matrix)\n",
        "    if isinstance(result, str):\n",
        "        print(result)\n",
        "    else:\n",
        "        print(\"Solusi:\")\n",
        "        for i, x in enumerate(result):\n",
        "            print(f\"x{i+1} = {x:.2f}\")"
      ]
    }
  ]
}