from homework.swap_case.swap_case import swap_case


class TestSwapCase:

    def test_basic_mixed(self):
        assert (
            swap_case("HackerRank.com presents 'Pythonist 2'.")
            == "hACKERrANK.COM PRESENTS 'pYTHONIST 2'."
        )

    def test_numbers_and_letters(self):
        assert swap_case("22T6M2reD4") == "22t6m2REd4"

    def test_long_mixed_characters(self):
        assert (
            swap_case(
                "SG.2ehL62pSmsnd7c9XYYsFvV067gybBhsSM0SJ7zpAJWr8pwEFzq3ACtuSAjpL7ZnWXbASGlBnEawSnWs1 gpCySKB2.at bt5S"
            )
            == "sg.2EHl62PsMSND7C9xyySfVv067GYBbHSsm0sj7ZPajwR8PWefZQ3acTUsaJPl7zNwxBasgLbNeAWsNwS1 GPcYskb2.AT BT5s"
        )

    def test_long_with_special_characters(self):
        assert (
            swap_case(
                "K96.5GI.sabDH3s.6iFzxMAh5IPtmWJ4w0uJ9MOWC45eoZkhaSs73gxKoQcd90Uge02cAxPnyMWtYW'TRVcO.0VnBq.sIQ5HFhkx"
            )
            == "k96.5gi.SABdh3S.6IfZXmaH5ipTMwj4W0Uj9mowc45EOzKHAsS73GXkOqCD90uGE02CaXpNYmwTyw'trvCo.0vNbQ.Siq5hfHKX"
        )

    def test_special_characters(self):
        assert (
            swap_case(
                "hG4 KIm2ONx3x5epersw Dz.ytOVfXSxrh'MephUyRYAkHsDZOZStP'2XRv6XqcT0RkI5INrfr38 4BPUuS85OGWXNgXZPaHF1oy"
            )
            == "Hg4 kiM2onX3X5EPERSW dZ.YTovFxsXRH'mEPHuYryaKhSdzozsTp'2xrV6xQCt0rKi5inRFR38 4bpuUs85ogwxnGxzpAhf1OY"
        )

    def test_very_large_string(self):
        assert (
            swap_case(
                "OzD0ro.7xwq A.MqhqT7'evgaVjpQ36OjSwfhuMaME'SDlyjPttjr6knZURciDARzAZ.3hQeIvX'IPe875zS3su6dajlMnbQOiH37U3YG0uzy6vW4v.onodBDDREYOf3CqeHfGcCeWV0dXrmTWAUsuw'jVwFO'5n.jvKLwXaDsam'y5sVQqB5O16bn1ug1XFeg3kmOGQFjxQ524k Z0yv76b4kkaC YuW9cw8Sfjf4 ynhe N88N3N2pfJF.I4ec5PgTp0Mp6VKawzg7GctsbPmU73aERqHxvWOMxDGZI9XWnJV6Aumecv0bHopAmfeD1K vTcxkzmdypHOGcdELdXjINde.ICPhEnpr9nJVL M7uY'L0BDX0i7CNCjIt9OiE2xjXt7JkK7vdUFlp6qn3Zua5vfP'nJcbviLrwj3.VlDDkd4VQ6zV1G2sGMmTVYkzaR9z5CDujAl'zYw8jw 9VOb5dP'zT'UTLMX2u8OG5YrGrvcENXF'QhBC8Ti'KRuhuO'SLlDKuRPHxFtnXW27YY1BMN9YkQww9kloEb43'loYiSFpIPiA0f1.3RYNUEN4QSbNQMpwQPZXsVKhc.uGvGJHiU80gcvOufOI2A0LdPcwGBWjTDl4TBZaycMfCmOceYqPj gqV7wTfSkY1F4INWqlKez.Vzbf84htDJg6D4MUt 2cGy8gMQolE 3gLR.rh3s5nbzN8hqKJr4c0L48zm2Hm7ObgsDu8dlrHnDaVKLQ65a7oTyz D6MLYD.q2AQXnQHKuTxKu5Fq7iNIRZKYyYeZo8n8JwHXtDbOaEnu'4'vmAsf2XR2q0ozLdw2FVsVpKEm4KzigoxY2GOpZq3OYW8cboQoD7STPJ8B'yEGZgk0vT mBABj0xeckqn6'Ouo"
            )
            == "oZd0RO.7XWQ a.mQHQt7'EVGAvJPq36oJsWFHUmAme'sdLYJpTTJR6KNzurCIdarZaz.3HqEiVx'ipE875Zs3SU6DAJLmNBqoIh37u3yg0UZY6Vw4V.ONODbddreyoF3cQEhFgCcEwv0DxRMtwauSUW'JvWfo'5N.JVklWxAdSAM'Y5SvqQb5o16BN1UG1xfEG3KMogqfJXq524K z0YV76B4KKAc yUw9CW8sFJF4 YNHE n88n3n2PFjf.i4EC5pGtP0mP6vkAWZG7gCTSBpMu73AerQhXVwomXdgzi9xwNjv6aUMECV0BhOPaMFEd1k VtCXKZMDYPhogCDelDxJinDE.icpHeNPR9Njvl m7Uy'l0bdx0I7cncJiT9oIe2XJxT7jKk7VDufLP6QN3zUA5VFp'NjCBVIlRWJ3.vLddKD4vq6Zv1g2SgmMtvyKZAr9Z5cdUJaL'ZyW8JW 9voB5Dp'Zt'utlmx2U8og5yRgRVCenxf'qHbc8tI'krUHUo'slLdkUrphXfTNxw27yy1bmn9yKqWW9KLOeB43'LOyIsfPipIa0F1.3rynuen4qsBnqmPWqpzxSvkHC.UgVgjhIu80GCVoUFoi2a0lDpCWgbwJtdL4tbzAYCmFcMoCEyQpJ GQv7WtFsKy1f4inwQLkEZ.vZBF84HTdjG6d4muT 2CgY8GmqOLe 3Glr.RH3S5NBZn8HQkjR4C0l48ZM2hM7oBGSdU8DLRhNdAvklq65A7OtYZ d6mlyd.Q2aqxNqhkUtXkU5fQ7InirzkyYyEzO8N8jWhxTdBoAeNU'4'VMaSF2xr2Q0OZlDW2fvSvPkeM4kZIGOXy2goPzQ3oyw8CBOqOd7stpj8b'YegzGK0Vt MbabJ0XECKQN6'oUO"
        )
