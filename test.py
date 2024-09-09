def fcfs_page_replacement(page_requests, frame_size):
    frame = []
    page_faults = 0

    for page in page_requests:
        if page not in frame:
            page_faults += 1
            if len(frame) >= frame_size:
                frame.pop(0)
            frame.append(page)
        print(f"Page: {page}, Frame: {frame}")

    return page_faults
page_requests = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
frame_size = 4
page_faults = fcfs_page_replacement(page_requests, frame_size)
print(f"Total Page Faults: {page_faults}")
