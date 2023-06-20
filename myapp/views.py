
# Create your views here.
from django.shortcuts import render
from math import pi, cos, sin

def form_view(request):
    if request.method == 'POST':
        radius = request.POST.get('radius')
        x_center = request.POST.get('center_x')
        y_center = request.POST.get('center_y')
        num_segments = request.POST.get('num_segments')

        if radius is not None and x_center is not None and y_center is not None and num_segments is not None:
            radius = float(radius)
            x_center = float(x_center)
            y_center = float(y_center)
            num_segments = int(num_segments)

            angles = [2 * pi * i / num_segments for i in range(num_segments)]
            coordinates = [
                (
                    i+1,  # 追加した行番号
                    "{:.3f}".format(x_center + radius * cos(angle)),
                    "{:.3f}".format(y_center + radius * sin(angle))
                )
                for i, angle in enumerate(angles)  # enumerate を使ってインデックス (i) を取得
            ]

            return render(request, 'myapp/form.html', {'coordinates': coordinates})

    return render(request, 'myapp/form.html')
