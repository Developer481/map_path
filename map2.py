import streamlit as st
import folium
from geopy.distance import geodesic
import heapq
from streamlit_folium import folium_static

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def main():
    # Title and header
    st.title("Shortest Path Visualization")
    st.header("Enter Coordinates")

    # Input fields for coordinates
    coord_A = st.text_input("Coordinate A (lat, lon)", "(51.5074, -0.1278)")
    coord_B = st.text_input("Coordinate B (lat, lon)", "(48.8566, 2.3522)")
    coord_C = st.text_input("Coordinate C (lat, lon)", "(41.9028, 12.4964)")
    coord_D = st.text_input("Coordinate D (lat, lon)", "(40.7128, -74.0060)")
    coord_E = st.text_input("Coordinate E (lat, lon)", "(43.7128, -74.0060)")  # Add additional input fields as needed
    coord_F = st.text_input("Coordinate F (lat, lon)", "(44.7128, -74.0060)")
    coord_G = st.text_input("Coordinate G (lat, lon)", "(45.7128, -74.0060)")
    coord_H = st.text_input("Coordinate H (lat, lon)", "(46.7128, -74.0060)")
    coord_I = st.text_input("Coordinate I (lat, lon)", "(47.7128, -74.0060)")
    coord_J = st.text_input("Coordinate J (lat, lon)", "(48.7128, -74.0060)")
    coord_K = st.text_input("Coordinate K (lat, lon)", "(49.7128, -74.0060)")
    coord_L = st.text_input("Coordinate L (lat, lon)", "(50.7128, -74.0060)")
    coord_M = st.text_input("Coordinate M (lat, lon)", "(51.7128, -74.0060)")
    coord_N = st.text_input("Coordinate N (lat, lon)", "(52.7128, -74.0060)")

    # Convert input strings to coordinate tuples
    coord_A = tuple(float(x) for x in coord_A.strip("()").split(","))
    coord_B = tuple(float(x) for x in coord_B.strip("()").split(","))
    coord_C = tuple(float(x) for x in coord_C.strip("()").split(","))
    coord_D = tuple(float(x) for x in coord_D.strip("()").split(","))
    coord_E = tuple(float(x) for x in coord_E.strip("()").split(","))  # Convert additional coordinate inputs to tuples
    coord_F = tuple(float(x) for x in coord_F.strip("()").split(","))
    coord_G = tuple(float(x) for x in coord_G.strip("()").split(","))
    coord_H = tuple(float(x) for x in coord_H.strip("()").split(","))
    coord_I = tuple(float(x) for x in coord_I.strip("()").split(","))
    coord_J = tuple(float(x) for x in coord_J.strip("()").split(","))
    coord_K = tuple(float(x) for x in coord_K.strip("()").split(","))
    coord_L = tuple(float(x) for x in coord_L.strip("()").split(","))
    coord_M = tuple(float(x) for x in coord_M.strip("()").split(","))
    coord_N = tuple(float(x) for x in coord_N.strip("()").split(","))

    # Create the graph using the input coordinates
    graph = {
        coord_A: {coord_B: calculate_distance(coord_A, coord_B),
                  coord_C: calculate_distance(coord_A, coord_C),
                  coord_D: calculate_distance(coord_A, coord_D),
                  coord_E: calculate_distance(coord_A, coord_E),
                  coord_F: calculate_distance(coord_A, coord_F),
                  coord_G: calculate_distance(coord_A, coord_G),
                  coord_H: calculate_distance(coord_A, coord_H),
                  coord_I: calculate_distance(coord_A, coord_I),
                  coord_J: calculate_distance(coord_A, coord_J),
                  coord_K: calculate_distance(coord_A, coord_K),
                  coord_L: calculate_distance(coord_A, coord_L),
                  coord_M: calculate_distance(coord_A, coord_M),
                  coord_N: calculate_distance(coord_A, coord_N)},
        coord_B: {coord_A: calculate_distance(coord_B, coord_A),
                  coord_C: calculate_distance(coord_B, coord_C),
                  coord_D: calculate_distance(coord_B, coord_D),
                  coord_E: calculate_distance(coord_B, coord_E),
                  coord_F: calculate_distance(coord_B, coord_F),
                  coord_G: calculate_distance(coord_B, coord_G),
                  coord_H: calculate_distance(coord_B, coord_H),
                  coord_I: calculate_distance(coord_B, coord_I),
                  coord_J: calculate_distance(coord_B, coord_J),
                  coord_K: calculate_distance(coord_B, coord_K),
                  coord_L: calculate_distance(coord_B, coord_L),
                  coord_M: calculate_distance(coord_B, coord_M),
                  coord_N: calculate_distance(coord_B, coord_N)},
        coord_C: {coord_A: calculate_distance(coord_C, coord_A),
                  coord_B: calculate_distance(coord_C, coord_B),
                  coord_D: calculate_distance(coord_C, coord_D),
                  coord_E: calculate_distance(coord_C, coord_E),
                  coord_F: calculate_distance(coord_C, coord_F),
                  coord_G: calculate_distance(coord_C, coord_G),
                  coord_H: calculate_distance(coord_C, coord_H),
                  coord_I: calculate_distance(coord_C, coord_I),
                  coord_J: calculate_distance(coord_C, coord_J),
                  coord_K: calculate_distance(coord_C, coord_K),
                  coord_L: calculate_distance(coord_C, coord_L),
                  coord_M: calculate_distance(coord_C, coord_M),
                  coord_N: calculate_distance(coord_C, coord_N)},
        coord_D: {coord_A: calculate_distance(coord_D, coord_A),
                  coord_B: calculate_distance(coord_D, coord_B),
                  coord_C: calculate_distance(coord_D, coord_C),
                  coord_E: calculate_distance(coord_D, coord_E),
                  coord_F: calculate_distance(coord_D, coord_F),
                  coord_G: calculate_distance(coord_D, coord_G),
                  coord_H: calculate_distance(coord_D, coord_H),
                  coord_I: calculate_distance(coord_D, coord_I),
                  coord_J: calculate_distance(coord_D, coord_J),
                  coord_K: calculate_distance(coord_D, coord_K),
                  coord_L: calculate_distance(coord_D, coord_L),
                  coord_M: calculate_distance(coord_D, coord_M),
                  coord_N: calculate_distance(coord_D, coord_N)},
        coord_E: {coord_A: calculate_distance(coord_E, coord_A),
                  coord_B: calculate_distance(coord_E, coord_B),
                  coord_C: calculate_distance(coord_E, coord_C),
                  coord_D: calculate_distance(coord_E, coord_D),
                  coord_F: calculate_distance(coord_E, coord_F),
                  coord_G: calculate_distance(coord_E, coord_G),
                  coord_H: calculate_distance(coord_E, coord_H),
                  coord_I: calculate_distance(coord_E, coord_I),
                  coord_J: calculate_distance(coord_E, coord_J),
                  coord_K: calculate_distance(coord_E, coord_K),
                  coord_L: calculate_distance(coord_E, coord_L),
                  coord_M: calculate_distance(coord_E, coord_M),
                  coord_N: calculate_distance(coord_E, coord_N)},
        coord_F: {coord_A: calculate_distance(coord_F, coord_A),
                  coord_B: calculate_distance(coord_F, coord_B),
                  coord_C: calculate_distance(coord_F, coord_C),
                  coord_D: calculate_distance(coord_F, coord_D),
                  coord_E: calculate_distance(coord_F, coord_E),
                  coord_G: calculate_distance(coord_F, coord_G),
                  coord_H: calculate_distance(coord_F, coord_H),
                  coord_I: calculate_distance(coord_F, coord_I),
                  coord_J: calculate_distance(coord_F, coord_J),
                  coord_K: calculate_distance(coord_F, coord_K),
                  coord_L: calculate_distance(coord_F, coord_L),
                  coord_M: calculate_distance(coord_F, coord_M),
                  coord_N: calculate_distance(coord_F, coord_N)},
        coord_G: {coord_A: calculate_distance(coord_G, coord_A),
                  coord_B: calculate_distance(coord_G, coord_B),
                  coord_C: calculate_distance(coord_G, coord_C),
                  coord_D: calculate_distance(coord_G, coord_D),
                  coord_E: calculate_distance(coord_G, coord_E),
                  coord_F: calculate_distance(coord_G, coord_F),
                  coord_H: calculate_distance(coord_G, coord_H),
                  coord_I: calculate_distance(coord_G, coord_I),
                  coord_J: calculate_distance(coord_G, coord_J),
                  coord_K: calculate_distance(coord_G, coord_K),
                  coord_L: calculate_distance(coord_G, coord_L),
                  coord_M: calculate_distance(coord_G, coord_M),
                  coord_N: calculate_distance(coord_G, coord_N)},
        coord_H: {coord_A: calculate_distance(coord_H, coord_A),
                  coord_B: calculate_distance(coord_H, coord_B),
                  coord_C: calculate_distance(coord_H, coord_C),
                  coord_D: calculate_distance(coord_H, coord_D),
                  coord_E: calculate_distance(coord_H, coord_E),
                  coord_F: calculate_distance(coord_H, coord_F),
                  coord_G: calculate_distance(coord_H, coord_G),
                  coord_I: calculate_distance(coord_H, coord_I),
                  coord_J: calculate_distance(coord_H, coord_J),
                  coord_K: calculate_distance(coord_H, coord_K),
                  coord_L: calculate_distance(coord_H, coord_L),
                  coord_M: calculate_distance(coord_H, coord_M),
                  coord_N: calculate_distance(coord_H, coord_N)},
        coord_I: {coord_A: calculate_distance(coord_I, coord_A),
                  coord_B: calculate_distance(coord_I, coord_B),
                  coord_C: calculate_distance(coord_I, coord_C),
                  coord_D: calculate_distance(coord_I, coord_D),
                  coord_E: calculate_distance(coord_I, coord_E),
                  coord_F: calculate_distance(coord_I, coord_F),
                  coord_G: calculate_distance(coord_I, coord_G),
                  coord_H: calculate_distance(coord_I, coord_H),
                  coord_J: calculate_distance(coord_I, coord_J),
                  coord_K: calculate_distance(coord_I, coord_K),
                  coord_L: calculate_distance(coord_I, coord_L),
                  coord_M: calculate_distance(coord_I, coord_M),
                  coord_N: calculate_distance(coord_I, coord_N)},
        coord_J: {coord_A: calculate_distance(coord_J, coord_A),
                  coord_B: calculate_distance(coord_J, coord_B),
                  coord_C: calculate_distance(coord_J, coord_C),
                  coord_D: calculate_distance(coord_J, coord_D),
                  coord_E: calculate_distance(coord_J, coord_E),
                  coord_F: calculate_distance(coord_J, coord_F),
                  coord_G: calculate_distance(coord_J, coord_G),
                  coord_H: calculate_distance(coord_J, coord_H),
                  coord_I: calculate_distance(coord_J, coord_I),
                  coord_K: calculate_distance(coord_J, coord_K),
                  coord_L: calculate_distance(coord_J, coord_L),
                  coord_M: calculate_distance(coord_J, coord_M),
                  coord_N: calculate_distance(coord_J, coord_N)},
        coord_K: {coord_A: calculate_distance(coord_K, coord_A),
                  coord_B: calculate_distance(coord_K, coord_B),
                  coord_C: calculate_distance(coord_K, coord_C),
                  coord_D: calculate_distance(coord_K, coord_D),
                  coord_E: calculate_distance(coord_K, coord_E),
                  coord_F: calculate_distance(coord_K, coord_F),
                  coord_G: calculate_distance(coord_K, coord_G),
                  coord_H: calculate_distance(coord_K, coord_H),
                  coord_I: calculate_distance(coord_K, coord_I),
                  coord_J: calculate_distance(coord_K, coord_J),
                  coord_L: calculate_distance(coord_K, coord_L),
                  coord_M: calculate_distance(coord_K, coord_M),
                  coord_N: calculate_distance(coord_K, coord_N)},
        coord_L: {coord_A: calculate_distance(coord_L, coord_A),
                  coord_B: calculate_distance(coord_L, coord_B),
                  coord_C: calculate_distance(coord_L, coord_C),
                  coord_D: calculate_distance(coord_L, coord_D),
                  coord_E: calculate_distance(coord_L, coord_E),
                  coord_F: calculate_distance(coord_L, coord_F),
                  coord_G: calculate_distance(coord_L, coord_G),
                  coord_H: calculate_distance(coord_L, coord_H),
                  coord_I: calculate_distance(coord_L, coord_I),
                  coord_J: calculate_distance(coord_L, coord_J),
                  coord_K: calculate_distance(coord_L, coord_K),
                  coord_M: calculate_distance(coord_L, coord_M),
                  coord_N: calculate_distance(coord_L, coord_N)},
        coord_M: {coord_A: calculate_distance(coord_M, coord_A),
                  coord_B: calculate_distance(coord_M, coord_B),
                  coord_C: calculate_distance(coord_M, coord_C),
                  coord_D: calculate_distance(coord_M, coord_D),
                  coord_E: calculate_distance(coord_M, coord_E),
                  coord_F: calculate_distance(coord_M, coord_F),
                  coord_G: calculate_distance(coord_M, coord_G),
                  coord_H: calculate_distance(coord_M, coord_H),
                  coord_I: calculate_distance(coord_M, coord_I),
                  coord_J: calculate_distance(coord_M, coord_J),
                  coord_K: calculate_distance(coord_M, coord_K),
                  coord_L: calculate_distance(coord_M, coord_L),
                  coord_N: calculate_distance(coord_M, coord_N)},
        coord_N: {coord_A: calculate_distance(coord_N, coord_A),
                  coord_B: calculate_distance(coord_N, coord_B),
                  coord_C: calculate_distance(coord_N, coord_C),
                  coord_D: calculate_distance(coord_N, coord_D),
                  coord_E: calculate_distance(coord_N, coord_E),
                  coord_F: calculate_distance(coord_N, coord_F),
                  coord_G: calculate_distance(coord_N, coord_G),
                  coord_H: calculate_distance(coord_N, coord_H),
                  coord_I: calculate_distance(coord_N, coord_I),
                  coord_J: calculate_distance(coord_N, coord_J),
                  coord_K: calculate_distance(coord_N, coord_K),
                  coord_L: calculate_distance(coord_N, coord_L),
                  coord_M: calculate_distance(coord_N, coord_M)}
    }

    start_vertex = coord_A
    shortest_distances = dijkstra(graph, start_vertex)

    # Create a folium map centered at the starting location
    map_center = coord_A
    mymap = folium.Map(location=map_center, zoom_start=10)

    # Add markers for each vertex
    for vertex, distance in shortest_distances.items():
        folium.Marker(location=vertex, tooltip=f"Distance: {distance:.2f} km").add_to(mymap)

    # Create a list of coordinates for the path
    path_coordinates = list(shortest_distances.keys())

    # Add a polyline to represent the path
    folium.PolyLine(locations=path_coordinates, color='blue').add_to(mymap)

    # Render the map visualization in Streamlit
    folium_static(mymap)


if __name__ == '__main__':
    main()
