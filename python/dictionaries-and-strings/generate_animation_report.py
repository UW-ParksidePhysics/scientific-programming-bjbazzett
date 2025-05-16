"""reads the source file and snips it up"""
def parse_animation_code(code_filename):
    with open(code_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    snippets = []
    snippet = []
    for line in lines:
        if line.strip() == '' and snippet:
            snippets.append(''.join(snippet))
            snippet = []
        else:
            snippet.append(line)
    if snippet:
        snippets.append(''.join(snippet))
    return snippets

"""formats the string"""
def format_section_header(header_string):
    return f"<h1>{header_string}</h1>\n"

"""writes the full report string"""
def write_html_report(report_string, report_filename):
    with open(report_filename, 'w', encoding='utf-8') as file:
        file.write(report_string)

""""temperature function that generates plots"""
def generate_static_plots(code_function, time_values, output_filenames):
    import matplotlib.pyplot as plt
    import numpy as np
    depth_array = np.linspace(0, 5, 300)
    for t_sec, output_file in zip(time_values, output_filenames):
        temp_profile = code_function(depth_array, t_sec)
        plt.figure()
        plt.plot(temp_profile, depth_array)
        plt.gca().invert_yaxis()
        plt.title(f"Temperature Profile at t = {t_sec / 3600:.1f} hours")
        plt.xlabel("Temperature (°C)")
        plt.ylabel("Depth (m)")
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()

"""importing temp, animating the gif, and compiling the html codee"""
def main():
    code_filename = "animate_heat_wave.py"
    report_filename = "animation_report.html"
    gif_filename = "heat_wave.gif"
    static_plot_files = ["plot_time_0.png", "plot_time_1.png", "plot_time_2.png"]
    time_values = [0, 6 * 3600, 18 * 3600]  # 0h, 6h, 18h
    from animate_heat_wave import compute_temperature
    generate_static_plots(compute_temperature, time_values, static_plot_files)
    html = "<html>\n<head><title>Heat Wave Animation Report</title></head>\n<body>\n"
    html += format_section_header("Python Program: animate_heat_wave.py")
    code_snippets = parse_animation_code(code_filename)
    for snippet in code_snippets:
        html += "<pre>\n" + snippet + "</pre>\n"
    html += format_section_header("Static Temperature Profiles at Different Times")
    for image_file in static_plot_files:
        html += f'<p><img src="{image_file}" width="600"></p>\n'
    html += format_section_header("Animated Heat Wave GIF")
    html += f'<p><img src="{gif_filename}" width="600"></p>\n'
    html += "</body>\n</html>"
    write_html_report(html, report_filename)
    print(f"Report saved to {report_filename}")

if __name__ == '__main__':
    main()