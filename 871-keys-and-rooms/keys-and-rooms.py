class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        st=[0]
        visited=set()
        while st:
            ele=st.pop()
            visited.add(ele)
            for key in rooms[ele]:
                if key not in visited:
                    st.append(key)
        return len(visited) == len(rooms)
        
        