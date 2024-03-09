# Bye-Pair Encoding
import string

with open("e.txt", "r", encoding="utf-8") as f:
    text = f.read()

n_iters = 4
idx, idx2 = 0, 0
lst = []
alphabets = string.ascii_letters
for t in list(set(text.split())):
    txt = t[:]

    for idx3 in range(n_iters):
        z = {}
        for maxlen in range(2, 10):
            x = set([txt[i:i + maxlen] for i in range(0, len(txt), maxlen)])
            y = {i: txt.count(i) for i in x if txt.count(i) > 1}
            if not y:
                break

            z[maxlen] = len(y)

        if not any(z.values()):
            break

        best_len = max([k for k, v in z.items() if v == max(z.values())], default=None)

        if best_len is None:
            break

        x = set([txt[i:i + best_len] for i in range(0, len(txt), best_len)])
        y = {i: txt.count(i) for i in x if txt.count(i) > 1}

        for i in y.keys():
            replacement = f"{idx2}{alphabets[idx % len(alphabets)]}"
            new_t = txt.replace(i, replacement)

            if new_t != txt:
                # print(f"{replacement} -> {i}")
                txt = new_t
                idx += 1

                if idx3 == n_iters - 1:
                    lst.append(txt)

                if idx % len(alphabets) == 0:
                    idx2 += 1

print(lst)
print(len(lst))
print(len(list(set(text.split()))))
