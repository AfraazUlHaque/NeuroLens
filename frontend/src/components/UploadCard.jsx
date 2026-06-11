import { useState } from "react";
import axios from "axios";

function UploadCard({ setResult, setLoading }) {

    const [file, setFile] = useState(null);
    const [dragActive, setDragActive] = useState(false);


    // Handle file selection
    const handleFile = (selectedFile) => {

        if (!selectedFile) return;

        const name = selectedFile.name.toLowerCase();

        if (
            name.endsWith(".nii") ||
            name.endsWith(".nii.gz")
        ) {
            setFile(selectedFile);
        }
        else {
            alert("Only .nii or .nii.gz files allowed");
        }
    };


    // Drag events
    const handleDrag = (e) => {
        e.preventDefault();
        e.stopPropagation();
    };


    const handleDragEnter = (e) => {
        handleDrag(e);
        setDragActive(true);
    };


    const handleDragLeave = (e) => {
        handleDrag(e);
        setDragActive(false);
    };


    const handleDrop = (e) => {

        handleDrag(e);

        setDragActive(false);

        const droppedFile = e.dataTransfer.files[0];

        handleFile(droppedFile);
    };


    // Upload MRI
    const handleUpload = async () => {

        if (!file) {
            alert("Please select an MRI file");
            return;
        }


        const formData = new FormData();

        formData.append("file", file);


        try {

            setLoading(true);


            const response = await axios.post(
                "http://127.0.0.1:8000/predict",
                formData,
                {
                    headers: {
                        "Content-Type":
                        "multipart/form-data"
                    }
                }
            );


            setResult(response.data.data);


        } catch (error) {

            console.error(error);

            alert("Analysis failed");

        } finally {

            setLoading(false);
        }
    };


    return (

        <div className="
            card
            rounded-3xl
            p-8
            max-w-xl
            mx-auto
            text-center
        ">


            <h2 className="
                text-3xl 
                font-bold 
                mb-3">
                Upload MRI Scan
            </h2>


            <p className="
                text-gray-300 
                mb-6">
                Drag your MRI scan here or click to browse
            </p>


            {/* Hidden input */}
            <input
                id="mriFile"
                type="file"
                accept=".nii,.nii.gz"
                className="hidden"

                onChange={(e)=>
                    handleFile(
                        e.target.files[0]
                    )
                }
            />


            {/* Drag Area */}
            <label

                htmlFor="mriFile"

                onDragEnter={handleDragEnter}
                onDragOver={handleDrag}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}

                className={`
                    block
                    cursor-pointer
                    rounded-2xl
                    border-2
                    border-dashed
                    p-10
                    transition-all
                    duration-300

                    ${
                        dragActive
                        ?
                        "border-cyan-400 bg-cyan-500/20"
                        :
                        "border-gray-500 hover:border-cyan-400"
                    }
                `}
            >


                <div className="text-5xl">
                    
                </div>


                <p className="
                    mt-4
                    text-lg">

                    {
                        file
                        ?
                        `✓ ${file.name}`
                        :
                        "Drop MRI file here"
                    }

                </p>


                <p className="
                    text-sm
                    text-gray-400
                    mt-2">

                    Supported formats:
                    .nii / .nii.gz

                </p>


            </label>


            <button

                onClick={handleUpload}

                disabled={!file}

                className={`
                    mt-6
                    px-8
                    py-3
                    rounded-xl
                    font-semibold
                    transition

                    ${
                        file
                        ?
                        "bg-cyan-500 hover:bg-cyan-600"
                        :
                        "bg-gray-600 cursor-not-allowed"
                    }
                `}

            >

                Analyze with AI

            </button>


        </div>
    );
}


export default UploadCard;