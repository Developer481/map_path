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

    # Convert input strings to coordinate tuples
    coord_A = tuple(float(x) for x in coord_A.strip("()").split(","))
    coord_B = tuple(float(x) for x in coord_B.strip("()").split(","))
    coord_C = tuple(float(x) for x in coord_C.strip("()").split(","))
    coord_D = tuple(float(x) for x in coord_D.strip("()").split(","))

    # Create the graph using the input coordinates
    graph = {
        coord_A: {coord_B: calculate_distance(coord_A, coord_B),
                  coord_C: calculate_distance(coord_A, coord_C)},
        coord_B: {coord_A: calculate_distance(coord_B, coord_A),
                  coord_C: calculate_distance(coord_B, coord_C),
                  coord_D: calculate_distance(coord_B, coord_D)},
        coord_C: {coord_A: calculate_distance(coord_C, coord_A),
                  coord_B: calculate_distance(coord_C, coord_B),
                  coord_D: calculate_distance(coord_C, coord_D)},
        coord_D: {coord_B: calculate_distance(coord_D, coord_B),
                  coord_C: calculate_distance(coord_D, coord_C),
                  coord_D: calculate_distance(coord_D, coord_D)},
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
